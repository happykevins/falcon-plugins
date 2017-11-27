#! /usr/bin/env python
#-*- coding:utf-8 -*-

import os
import json
import time

data = [
        {
            'metric': 'tthl.common.cu',
            'endpoint': '',
            'timestamp': int(time.time()),
            'step': 60,
            #'value': int(os.popen("who | wc -l").read().strip()),
	    'value': int(os.popen("netstat -anpt | grep \"8889\" | grep ESTABLISHED | wc -l").read().strip()),
            'counterType': 'GAUGE',
            }
        ]

print(json.dumps(data))
