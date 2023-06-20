#!/usr/bin/env python3

import psycopg2
import datetime
#from datetime import timedelta
import time
import os
import json


f = open('/usr/lib/xymon/server/ext/States/Arkansas/arkansas.json')
state = json.load(f)
ip = state['ip']

try:
    connection = psycopg2.connect(user="postgres",
                                  host=ip,
                                  port="5432",
                                  database="postgres")
    
    cursor = connection.cursor()
    postgreSQL_select_Query = "select (now() - pg_last_xact_replay_timestamp())::text AS replication_delay"
    cursor.execute(postgreSQL_select_Query)
    records = cursor.fetchone()
    delta = records[0]
    print (delta)
    ch = '.'
    z = delta.replace("-", '')
    print (z)


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
    COLOR = "red"
    cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
    TEST = "replication-status",
    BB = os.environ["BB"],
    BBDISP = os.environ["BBDISP"],
    COLOR = COLOR,
    NOW = datetime.datetime.now(),
    #NOW = error,
    MSG = error,
    NODE= "Arkansas-Traceability")
    os.system(cmd)
    print(cmd)

else:

    COLOR = "green"
    cmd = "{BB} {BBDISP} \"status {NODE}.{TEST} {COLOR} {NOW}\n {MSG}\n\"".format(
    TEST = "replication-status",
    BB = os.environ["BB"],
    BBDISP = os.environ["BBDISP"],
    NOW = datetime.datetime.now(),
    #NOW = "Replication is normal.",
    COLOR = COLOR,
    MSG = "time : " + z,
    NODE= "Arkansas-Traceability")
    os.system(cmd)
    print(cmd)

  
finally:
  print("Done.")

