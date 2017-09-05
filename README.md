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





Create some cpu load
`fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null & }; fulload; read; killall dd`
