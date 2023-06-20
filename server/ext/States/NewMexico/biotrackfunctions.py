# biotrackfunctions.py>
import os

def greenApi(node,test,misc,msg):
   print(node,test,misc,msg)
   COLOR = "green"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = msg,
   NODE = node)
   os.system(cmd)
   print(cmd)
   exit()


def redApi(node,test,misc,msg):
   print(node,test,misc,msg)
   COLOR = "red"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = msg,
   NODE = node)
   os.system(cmd)
   print(cmd)
   exit()

def slowApi(node,test,misc,msg):
   print(node,test,misc,msg)
   COLOR = "yellow"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = msg,
   NODE = node)
   os.system(cmd)
   print(cmd)
   exit()

#def exceptionApi(node,test,misc,msg):
#   print(node,test,misc,msg)
#   COLOR = "red"
#   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
#   TEST = test,
#   BB = os.environ["BB"],
#   BBDISP = os.environ["BBDISP"],
#   COLOR = COLOR,
#   NOW = misc,
#   MSG = msg, NODE = node) 
#   os.system(cmd)
#   print(cmd)
#   exit()

def redHttpCheck(node,test,misc,msg):
   f = open("/usr/lib/xymon/server/ext/States/Arkansas/redhttpcheck.txt", "w")
   L = "CRITICAL ERROR with Arkansas Traceability main site.\n", " Recheck again: https://arstems.arkansas.gov\n" 
   #f.write(s)
   f.writelines(L)
   f.close()
   g = open("/usr/lib/xymon/server/ext/States/Arkansas/redhttpcheck.txt", "r")
   file_content = g.read()
   COLOR = "red"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = file_content, 
   #MSG = "time : " +  msg + " seconds", 
   NODE = node) 
   os.system(cmd)
   g.close()
   print(cmd)
   exit()

def greenHttpCheck(node,test,misc,msg):
   f = open("/usr/lib/xymon/server/ext/States/Arkansas/green.txt", "w")
   L = "https://arstems.arkansas.gov\n", " time : " +  msg + " seconds\n", " Normal response opening main site.\n"
   #f.write(s)
   f.writelines(L)
   f.close()
   g = open("/usr/lib/xymon/server/ext/States/Arkansas/green.txt", "r")
   file_content = g.read()
   COLOR = "green"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = file_content, 
   #MSG = "time : " +  msg + " seconds", 
   NODE = node) 
   os.system(cmd)
   g.close()
   print(cmd)
   exit()
   

def bad_socket(msg,now):

   f = open("/usr/lib/xymon/server/ext/States/Arkansas/red.txt", "r")
   file_content = f.read()
   COLOR = "red"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = "httpcheck",
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = now, 
   MSG = file_content,
   NODE = "Arkansas")
   os.system(cmd)
   print(cmd)
   exit()

def greenApiCheck(node,test,misc,msg):
   f = open("/usr/lib/xymon/server/ext/States/Arkansas/greenapi.txt", "w")
   L = "https://arstems.arkansas.gov/serverxml.asp\n", " time : " +  msg + " seconds\n", " Normal response authenticating to the API.\n"
   #f.write(s)
   f.writelines(L)
   f.close()
   g = open("/usr/lib/xymon/server/ext/States/Arkansas/greenapi.txt", "r")
   file_content = g.read()
   COLOR = "green"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = file_content, 
   #MSG = "time : " +  msg + " seconds", 
   NODE = node) 
   os.system(cmd)
   g.close()
   print(cmd)
   exit()

def yellowApiCheck(node,test,misc,msg):
   f = open("/usr/lib/xymon/server/ext/States/Arkansas/yellowapi.txt", "w")
   L = "WARNING:Arkansas API is slow\n" " https://arstems.arkansas.gov/serverxml.asp\n", " time : " +  msg + " seconds\n"
   #f.write(s)
   f.writelines(L)
   f.close()
   g = open("/usr/lib/xymon/server/ext/States/Arkansas/yellowapi.txt", "r")
   file_content = g.read()
   COLOR = "yellow"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = file_content, 
   #MSG = "time : " +  msg + " seconds", 
   NODE = node) 
   os.system(cmd)
   g.close()
   print(cmd)
   exit()

def exceptionApi(node,test,misc,msg):
   f = open("/usr/lib/xymon/server/ext/States/Arkansas/badsocketcheck.txt", "w")
   L = "https://arstems.arkansas.gov/serverxml.asp\n", "  error: Connection-timeout\n", " Critical\n"
   #f.write(s)
   f.writelines(L)
   f.close()
   g = open("/usr/lib/xymon/server/ext/States/Arkansas/badsocketcheck.txt", "r")
   file_content = g.read()
   COLOR = "red"
   cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
   TEST = test,
   BB = os.environ["BB"],
   BBDISP = os.environ["BBDISP"],
   COLOR = COLOR,
   NOW = misc,
   MSG = file_content, 
   #MSG = "time : " +  msg + " seconds", 
   NODE = node) 
   os.system(cmd)
   g.close()
   print(cmd)
   exit()
