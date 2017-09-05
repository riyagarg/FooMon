## Real time system monitoring

A service to monitor system metrics at near real time ( lag ~ 1 min ).

What metrics are we talking about ?
- Any, they may be
- System level metrics like cpu, disk free % , disk used % , mysql reads , mysql writes , zookeeper stuffs , network IO
- Application level metrices : API hits per second , latency per api , heap free % and anything that you can imagine.

There are three primary components of the service :
- The hosts that run your application , EC2 containers , vms on bare metals , vms on aws boxes ... basically anything with a linux kernel ( raspberry pi too )
- The aggregator db : this is a graphite db. (Kick ass. Chew bubblegum. Make it easy to store and graph metrics.)
- Grafana : Visualizations reloaded.

### Local setup :

1. Setting up graphite database
```
cd graphite_host ;
vagrant up
```      
This will spawn a an ubuntu xenial64 machine with 2gb ram.

2. Setting up grafana visualizer
3. Setting up a sample host





Create some cpu load
`fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null & }; fulload; read; killall dd`
