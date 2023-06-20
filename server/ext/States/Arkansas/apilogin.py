#!/usr/bin/env python

import requests, json, xmltodict
import os
import time
import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring
from bs4 import BeautifulSoup
from biotrackfunctions import *

os.chdir("/usr/lib/xymon/server/ext/States/Arkansas")

f = open('/usr/lib/xymon/server/ext/States/Arkansas/arkansas.json')
state = json.load(f)

url = state['xml_url']
print (url)
state = state['a_folder']
api_test = state['arkansas-apitest']

request_url = url

headers = {
  'Content-Type':'text/xml'
  }

xml = '<xml>\
<API>4.0</API>\
<action>login</action>\
<password>Biotrack123!</password>\
<license_number>D0000000</license_number>\
<username>xymon@biotrackthc.com</username>\
<training>1</training>\
</xml>'

#a_folder
#a_path
#a_folder

startTime = time.time()
test = "arkansas-apitest"
state = "Arkansas"
a_path = '/usr/lib/xymon/server/ext/States/'
a_folder = "Arkansas"
xml_file = 'xml.xml'
joined_path_xml = os.path.join(a_path, a_folder, xml_file)

try:
    r = requests.post(request_url, data=xml, headers=headers)
    print (r)
    r.raise_for_status()
    xml = "xml"

    with open(joined_path_xml, 'w') as f:
        f.write(r.text)

    g = open(joined_path_xml, "r")

    executionTime = (time.time() - startTime)
    how_long = float(executionTime)

    my_str = str(print("%.2f" % how_long))

    xyz_file = 'xyz.txt'
    joined_path_xyz = os.path.join(a_path, a_folder, xyz_file)

    n = open(joined_path_xyz, "w")
    n.write(str(how_long) + '\n')

    catshit = round(how_long, 2)
    catshit = str(catshit)

    x = datetime.datetime.now()
    misc =  x.strftime("%c")

    soup = BeautifulSoup(g.read(), "xml")

    #print(soup)
    max = "2"
       

    if (soup.success.text == '1' and catshit < max ):
        msg = "time : " + catshit +" seconds", 
        node = "Arkansas"
        #greenApi(node,test,misc,msg)
        greenApiCheck(node,test,misc,catshit)


    elif (soup.success.text == '1' and catshit > max ): 
       COLOR = "yellow"
       node = "Arkansas"
       msg = "time : " + catshit +" seconds", 
       yellowApiCheck(node,test,misc,catshit)

    else: 
       (soup.success.text == '0')
       f = open(joined_path_xml, "r")
       file_contents = f.read()
       COLOR = "red"
       cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
       TEST = test,
       BB = os.environ["BB"],
       BBDISP = os.environ["BBDISP"],
       COLOR = COLOR,
       NOW = soup.error.text,
       MSG = "time : " + catshit, 
       NODE="Arkansas")
       os.system(cmd)
       print(cmd)
       g.close()

except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
    misc = "invalid http response"
    node = "Arkansas"
    exceptionApi(node,test,misc,errh)

except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
    misc = "either a network problem, dns failure or refused connections"
    node = "Arkansas"
    exceptionApi(node,test,misc,errc)

except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
    misc = "TimeOut Error"
    node = "Arkansas"
    exceptionApi(node,test,misc,errt)

except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
    misc = "Request-Exception"
    node = "Arkansas"
    exceptionApi(node,test,misc,err)

try:
    os.remove(joined_path_xml)
except OSError as e:
    print("Error: %s." % (e.strerror))

try:
    os.remove(joined_path_xyz)
except OSError as e:
    print("Error: %s." % (e.strerror))
