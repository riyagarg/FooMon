ubuntu@ubuntu-xenial:~$ sudo /etc/init.d/collectd status
● collectd.service - Statistics collection and monitoring daemon
   Loaded: loaded (/lib/systemd/system/collectd.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2017-09-05 17:38:53 UTC; 1min 21s ago
     Docs: man:collectd(1)
           man:collectd.conf(5)
           https://collectd.org
  Process: 18050 ExecStartPre=/usr/sbin/collectd -t (code=exited, status=0/SUCCESS)
 Main PID: 18055 (collectd)
    Tasks: 13
   Memory: 2.8M
      CPU: 161ms
   CGroup: /system.slice/collectd.service
           └─18055 /usr/sbin/collectd

Sep 05 17:39:13 ubuntu-xenial collectd[18055]: write_graphite plugin: Connecting to 192.168.33.70:2003 via tcp failed. The last error was: failed to connect to remote host: Connection refused
Sep 05 17:39:13 ubuntu-xenial collectd[18055]: bind plugin: curl_easy_perform failed: Failed to connect to localhost port 8053: Connection refused
Sep 05 17:39:13 ubuntu-xenial collectd[18055]: read-function of plugin `bind' failed. Will suspend it for 40.000 seconds.
Sep 05 17:39:13 ubuntu-xenial collectd[18055]: multimeter plugin: swrite failed.
Sep 05 17:39:13 ubuntu-xenial collectd[18055]: read-function of plugin `multimeter' failed. Will suspend it for 40.000 seconds.
Sep 05 17:39:43 ubuntu-xenial collectd[18055]: write_graphite plugin: Connecting to 192.168.33.70:2003 via tcp failed. The last error was: failed to connect to remote host: Connection refused
Sep 05 17:39:53 ubuntu-xenial collectd[18055]: bind plugin: curl_easy_perform failed: Failed to connect to localhost port 8053: Connection refused
Sep 05 17:39:53 ubuntu-xenial collectd[18055]: read-function of plugin `bind' failed. Will suspend it for 80.000 seconds.
Sep 05 17:39:53 ubuntu-xenial collectd[18055]: multimeter plugin: swrite failed.
Sep 05 17:39:53 ubuntu-xenial collectd[18055]: read-function of plugin `multimeter' failed. Will suspend it for 80.000 seconds.