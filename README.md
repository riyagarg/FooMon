# FooMon
---
## Real time system + application + metrics + events monitoring

A service to monitor system metrics at near real time.

### What metrics are we talking about ?

##### Many ... Any !
- System level metrics like cpu, disk free % , disk used % , mysql reads , mysql writes , zookeeper stuffs , network IO
- Application level metrices : API hits per second , latency per api , heap free % and anything that you can imagine.

There are three primary components of the service :
- The hosts that run your application , EC2 containers , vms on bare metals , vms on aws boxes ... basically anything with a linux kernel ( raspberry pi too )
- The aggregator db : this is a graphite db. (Kick ass. Chew bubblegum. Make it easy to store and graph metrics.)
- Grafana : Visualizations reloaded.

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
