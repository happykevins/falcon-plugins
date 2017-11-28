#! /usr/bin/env python
#-*- coding:utf-8 -*-

import os
import json
import time
import socket

data = [
        {
            'metric': 'tthl.common.cu',
            'endpoint': socket.gethostname(),
            'timestamp': int(time.time()),
            'step': 60,
            #'value': int(os.popen("who | wc -l").read().strip()),
	    'value': int(os.popen("netstat -anpt | grep \"8889\" | grep ESTABLISHED | wc -l").read().strip()),
            'counterType': 'GAUGE',
			"tags": "",
            }
        ]

print(json.dumps(data))
