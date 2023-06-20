#!/usr/bin/env python
import socket
import command
import datetime
import os
from os import system
import time
import re
import urllib.request
       
def bad_socket():  
   
   f = open("/usr/lib/xymon/server/ext/bad.txt", "r")
   file_contents = f.read()
   COLOR = "red"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = "checkHttps",
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = datetime.datetime.now(),
   MSG = file_contents,
   NODE="icheckurls")
   os.system(cmd)
   print(cmd)
   exit()

socket.setdefaulttimeout(3)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('il-uat01.biotrackthc.net', 443))
print(result)

if result != 0:
    bad_socket()

    ## Above is a socket connection, if it can't bind to port 443, the function will throw an alert and exit the script.
    ## benchmarking time execution
    
startTime = time.time()

with urllib.request.urlopen("https://il-uat01.biotrackthc.net") as url:
    s = url.read()
    #print(s)

    executionTime = (time.time() - startTime)
    how_long = float(executionTime)
    print("%.2f" % how_long)
    

    n = open("/usr/lib/xymon/server/ext/match.txt", "w")
    n.write(str(how_long) + '\n')
    n.close()

    x = datetime.datetime.now()
    shit =  x.strftime("%c")
    #Internal Error
    #Database error.

   
    if re.search(r'The Illinois Department of Agriculture has established', s.decode('utf-8')):   
       #print(s) 
       f = open("/usr/lib/xymon/server/ext/match.txt", "r")
       file_contents = f.read()
       COLOR = "green"
       cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
       TEST = "checkHttps",
       BB = os.environ["BB"],
       BBDISP = os.environ["BBDISP"],
       COLOR = COLOR,
       #NOW = datetime.datetime.now(),
       NOW = shit,
       MSG = file_contents,
       NODE="icheckurls")
       os.system(cmd)
       print(cmd)

    else:
   
       f = open("/usr/lib/xymon/server/ext/nomatch.txt", "r")
       print("shit")
       file_contents = f.read()
       COLOR = "red"
       cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
       TEST = "checkHttps",
       BB = os.environ["BB"],
       BBDISP = os.environ["BBDISP"],
       COLOR = COLOR,
       NOW = datetime.datetime.now(),
       MSG = file_contents,
       NODE="icheckurls")
       exit()
