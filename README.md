# FooMon
### Real time system + application + metrics + events monitoring
---
![ALL THE FUSS!](https://i.imgur.com/NVHRFu4.png)

---
### What is foomon ?
Foomon is a platform for data aggregation and visualisation.

### What powers foomon ?

Foomon has three essential components to it
1.  Producers.
2.  Consumer.
3.  Visualiser.


1.  **Producers** : 
    Anything that produces data for a given key. They can be one of the below three

    1.1 Applications : Microservices or services, Java , Ruby or node based applicaitions, 
    1.2 Servers :  Bare metals, vms or AWS hosts, this data ranges from cpu usage , entropy disk space, mysql read writes , kafka latencies and a huge number of other metrics.
    1.3 Custom cron jobs / On demand data : You can also pipe in data from custom shell scripts into the system to visualise it at a later point in time.

2.  **Consumer** : 

    A consumer is typically a graphite database that aggregates data from any or all of the given Producers and exposes a queriable interface.
    This is a nosql time series database. Any data has three essesntial components.

    - Key : That distinguishes this data from the rest of the other data sources.
    - Timestamp : A time series database will aggregate the data over a period of time.
    - Value : The value here refers to the value against the key.

    Hence to represent the data for a given metric, it would look like somewhat below
```
    | qa9.acx.cpu_usage | 1505922970 | 98.34 |
    | qa9.acx.cpu_usage | 1505922976 | 44.34 |
    | qa9.acx.cpu_usage | 1505922982 | 94.34 |
    | qa9.acx.cpu_usage | 1505922988 | 97.34 |

    This can be visualized as below for the key qa9.acx.cpu_usage as : 

    | TIMESTAMP  | VALUE |
    ----------------------
    | 1505922970 | 98.34 |
    | 1505922976 | 44.34 |
    | 1505922982 | 94.34 |
    | 1505922988 | 97.34 |
```
    The choice of the database used here is Graphite. There are other alternatives as well like influxdb , elasticsearch and the most popular OpenTSDB.
    OpenTSDB would is teh ideal candidate for an enterprise level architecture for its scalable and distributed nature, however it comes at the cost of an elaborate setup.

    Read more about the GraphiteDB here.

3.  **Visualizer** : 
    This is essentially a queriable interface to the abovementioned database.
    This is powered by Grafana.

    In Grafana all you need to do is to configure the data source once. Once you have setup the database, you are good to create dashboards on your own
    You can create custom dashboards, save as well as share dashboards.
    The dashboards can be saved as JSON objects that can be passed around as well.
    As of  right now, there are 32 data sources, 27 panels, 16 apps and 472 dashboards available to configure in grafana.
    Its supports real time query of data at intervals and has a wide variety of data source to read data from.

    https://github.com/grafana/grafana
    Grafana is distributed under Apache 2.0 License.

![Sample](https://camo.githubusercontent.com/d010ea19c70677a0bfd8a64fc01d2b0948e1ffc1/687474703a2f2f646f63732e67726166616e612e6f72672f6173736574732f696d672f66656174757265732f64617368626f6172645f6578312e706e67)  
  
  --- 
  
![Architecture](https://i.imgur.com/ZeQGC3U.png)

### Local setup :

- **Setting up graphite database**
  - `cd graphite_host && vagrant up`
  - This will spawn a an ubuntu xenial64 machine with 2gb ram.
  - Install docker.
  - Get graphite to run as a docker container with **NO** configuration.
  - The ip shall be `192.168.60.61`
  - For general knowledge : **2303** is the port of consumption of data.
  - Why docker inside vagrant ?  The vagrant box is a mimic of the ec2 container (not to be taken seriously)


- **Setting up _Grafana_ visualizer**
  - `cd grafana_host && vagrant up`
  - This will also spawn a an ubuntu xenial64 machine with 2gb ram.
  - Install grafana server
  - Start grafana server
  - It wll be availale at http://192.168.60.60:3000/
  - The username and passwords are `admin` and `admin` respectively.
  - Once up, head over to configure the data source.
  - Choose `graphite` as data source and then use http://192.168.60.60 with `direct`
  - Save and test.
  - You are good to go and create new dashboards.


- **Setting up a sample host**
  - `cd sample_host && vagrant up`
  - This will also spawn a an ubuntu xenial64 machine with 512mb ram.
  - Install `collectd`
  - once installed ssh into it with `vagrant ssh`
  - Once inside ... you need to configure your collectd so that it can relay all the system metrics automatically to the graphite_host
  - `sudo vim /etc/collectd/collectd.conf`
  - Uncomment : `LoadPlugin write_graphite`
  - Then head over to the part where the block reads like :
  ```
    <Plugin write_graphite>
      <Node "graphing">
          Host "localhost"
          Port "2003"
          Protocol "tcp"
          LogSendErrors true
          Prefix "collectd."
          StoreRates true
          AlwaysAppendDS false
          EscapeCharacter "_"
      </Node>
  </Plugin>
  ```
  
  - Once you are here you can have to set the `Host "localhost"` to `Host "192.168.60.61"`
  - This is the ip of the graphite database that you have setup.
  - We will tell Graphite to store collectd information at intervals of ten seconds for one day, at one minute for seven days, and intervals of ten minutes for one year.
  - This will give us a good balance between detailed information for recent activity and general trends over the long term. Collectd passes its metrics starting with the string collectd, so we will match that pattern.
  - The policy we described can be added by adding these lines. Remember, add these above the default policy, or else they will never be applied:
  
  ```
      [collectd]
      pattern = ^collectd.*
      retentions = 10s:1d,1m:7d,10m:1y
  ```
  
  - Get back to grafana and create a dashboard.

---

##### Create a test key and pass back some metrics with it

Run the `feeder.py` script after making changes to the line that reads:
`os.system('echo "Key.subkey '+randomdata+' `date +%s`" | nc 192.168.60.61 2003')`

This line means `Key.subkey` at `date +%s` timestamp has a value of `randomdata`
which is nothing but a random integer

---

##### Create some cpu load to test on dashboard

Run the command :

`fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null & }; fulload; read; killall dd`

---
