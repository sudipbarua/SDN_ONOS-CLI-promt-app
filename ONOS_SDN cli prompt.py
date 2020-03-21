#!/usr/bin/python
import os
import sys 
import json
import datetime
import math
import time
import signal
import requests
from requests.auth import HTTPBasicAuth
from cmd import Cmd


#---------------------------------------------------------------------#
#Topology Collector takes topology information from ONOS controller 
def TopoCollector():
    try:
      #Declare parameters for a GET request to ONOS controller
      url = 'http://localhost:8181/onos/v1/topology/'
      headers  = {"Accept": "application/json"}
      response = requests.get(url, headers = headers, auth=HTTPBasicAuth('onos', 'rocks'))
      #Parsing the response message
      for i in response.json():
	print i, ": ", response.json()[i]
	            
    except:
      print "There is an error"
#---------------------------------------------------------------------#

#---------------------------------------------------------------------#
#Particular Device Collector takes a device information from ONOS controller 
def ParticularDeviceCollector(DeviceID):
    try:
      #Declare parameters for a GET request to ONOS controller
      url = 'http://localhost:8181/onos/v1/devices/' + DeviceID
      headers  = {"Accept": "application/json"}
      response = requests.get(url, headers = headers, auth=HTTPBasicAuth('onos', 'rocks'))
      #Parsing the response message
      print "Reachable: ", response.json() ['available']
      print "Device uptime: ", response.json() ['humanReadableLastUpdate']
      print "ChassisID: ", response.json() ['chassisId']
      print "Vendor: ", response.json() ['mfr']
      print "Hardware Version: ", response.json() ['hw']
      print "Software Version: ", response.json() ['sw']
      print "Serial: ", response.json() ['serial']
      print "Protocol: ", response.json() ['annotations']['protocol']

    except:
      print "There is an error"
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
#Particular Host Collector takes a host information from ONOS controller 
def ParticularHostCollector(hostid):
    try:
      #Declare parameters for a GET request to ONOS controller
      url = 'http://localhost:8181/onos/v1/hosts/' + hostid
      headers  = {"Accept": "application/json"}
      response = requests.get(url, headers = headers, auth=HTTPBasicAuth('onos', 'rocks'))
      #Parsing the response message
      print "IP Address :", response.json()['ipAddresses']
      print "MAC Address :", response.json()['id']
      print "VLAN :", response.json()['vlan']
      
    except:
      print "There is an error"
#---------------------------------------------------------------------#


#---------------------------------------------------------------------#
#Statistic Collector takes flow statistics of a switch with a DeviceID from ONOS controller 
def StatsCollector(DeviceID):
  while True:
    try:
      #Declare parameters for a GET request to ONOS controller
      url = 'http://localhost:8181/onos/v1/flows/' + DeviceID
      headers  = {"Accept": "application/json"}
      response = requests.get(url, headers = headers, auth=HTTPBasicAuth('onos', 'rocks'))
      #Parsing the response message
      if response.json().has_key('flows'): 
        #See what information in inside
        for i in response.json()['flows']:
		for j in i:
			print j + ': ', i[j]
						
		print '\n'
      #Sleep 5.0 seconds and go for next requests
      time.sleep(5.0)
    except:
      print "There is an error"
      break
#---------------------------------------------------------------------#

#Onos CLI Prompt provides CLI interface to collect network data using simple command lines
class OnosCLIpromt(Cmd):
	def do_topology(self, inp):
        	#Get Topoloy information
        	TopoCollector()	
	def do_device1(self, inp):
        	#Get Switch 1 information
        	ParticularDeviceCollector("of:0000000000000001")
	def do_device2(self, inp):
        	#Get Switch 2 information
        	ParticularDeviceCollector("of:0000000000000002")
	def do_host1(self, inp):
        	#Get Host 1 information
        	ParticularHostCollector("EA:CE:5C:FC:42:FB/None")
	def do_host2(self, inp):
        	#Get Host 2 information
        	ParticularHostCollector("BE:9F:0F:7B:5E:E9/None")
	def do_stats_device1(self, inp):
		#Get statistics from switch 1
		StatsCollector("of:0000000000000001")
	def do_stats_device2(self, inp):
		#Get statistics from switch 2
		StatsCollector("of:0000000000000002")
	def emptyline(self):
		#Return nothing when empty line is given as an input
		pass
	def do_exit(self, inp):
		#Exit cli prompt and stop program
        	return True


if __name__ == '__main__':

  	OnosCLIpromt().cmdloop()


