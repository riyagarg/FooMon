#!/usr/bin/python

import time
import random
import os

while True:
    randomdata = str(random.randint(1,101))
    os.system('echo "Key.subkey '+randomdata+' `date +%s`" | nc 192.168.60.61 2003')
    print 'feeding in'+randomdata
    time.sleep(0.5)

