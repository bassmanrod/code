#!/usr/bin/env python
import socket
import command
import datetime
import os
from os import system
import time
import re
import urllib.request
import json
from biotrackfunctions import *

f = open('/usr/lib/xymon/server/ext/States/Arkansas/arkansas.json')
state           = json.load(f)

environment     = state['host']
url             = state['state_url']
production_site = state['environment']

host = state['host']
a_path = state['a_path']
a_folder = state['a_folder']

test = state['http_test']
regex = state['regex']     

prod_site = state['production_site']
x = datetime.datetime.now()
now =  x.strftime("%c")
print (now)
       
startTime = time.time()

socket.setdefaulttimeout(3)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((host, 443))

if result != 0:
#if result == 0:
    
    bad_socket(result,now)
    print (result)

else:
    executionTime = (time.time() - startTime)
    how_long = float(executionTime)
    crap = str("%.2f" % how_long)
    
try:
    with urllib.request.urlopen(url) as url:
        s = url.read()

except urllib.error.URLError as e:
         print (e)
        # handle timeout...
         bad_socket(e,now)
        #pass
   # raise e
   
if re.search(regex, s.decode('utf-8')):   
      
    greenHttpCheck(prod_site,test,now,crap)
    greenApiCheck(prod_site,test,now,crap)

else:
    redHttpCheck(prod_site,test,now,crap)
    print ("bad")
