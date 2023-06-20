#!/usr/bin/env python

import requests, json, xmltodict
import os
import time
import datetime
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring
from bs4 import BeautifulSoup

request_url = 'https://arstems.arkansas.gov/serverxml.asp'

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

startTime = time.time()
test = "ApiLogin"
state = "Arkansas"
a_path = '/usr/lib/xymon/server/ext/States/'
a_folder = 'Arkansas'
xml_file = 'xml.xml'
joined_path_xml = os.path.join(a_path, a_folder, xml_file)
print (joined_path_xml)

r = requests.post(request_url, data=xml, headers=headers)
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
shit =  x.strftime("%c")

soup = BeautifulSoup(g.read(), "xml")

print(soup)
max = "2"

if (soup.success.text == '1' and catshit < max ):
   f = open(joined_path_xml, "r")
   file_contents = f.read()
   COLOR = "green"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = shit,
   MSG = "time : " + catshit, 
   NODE="Arkansas-Traceability")
   os.system(cmd)
   print(cmd)

elif (soup.success.text == '1' and catshit > max ): 
    f = open(joined_path_xml, "r")
    file_contents = f.read()
    COLOR = "yellow"
    cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
    TEST = test,
    BB = os.environ["BB"],
    BBDISP = os.environ["BBDISP"],
    COLOR = COLOR,
    NOW = "slow",
    MSG = "time : " + catshit, 
    NODE="Arkansas-Traceability")
    os.system(cmd)
    print(cmd)

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
   NODE="Arkansas-Traceability")
   os.system(cmd)
   print(cmd)

g.close()

try:
    os.remove(joined_path_xml)
except OSError as e:
    print("Error: %s." % (e.strerror))

try:
    os.remove(joined_path_xyz)
except OSError as e:
    print("Error: %s." % (e.strerror))
