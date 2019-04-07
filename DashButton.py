#scapy needed to discover and recieve signal from Dash Button
from scapy.all import *
#Popen needed for applescipt integration in Python
from subprocess import Popen, PIPE
#requests used for webhooks with IFTTT
import requests
import datetime
import GoogleSheets
import AppNotification
import AppleScripts

#Static var for the MAC Address of Dash Button beacuse I'm lazy
DEVICE_MAC_ADDRESS = 'PUT MAC ADDRESS OF DASH BUTTON HERE'
thirdColumn = "Default Message"
SCRIPT = AppleScripts.SCRIPT
	
def device_found(packet_info):
	return DEVICE_MAC_ADDRESS == packet_info[ARP].hwsrc

def execute_action(packet_info, script=SCRIPT):
	if device_found(packet_info):
		AppNotification.send_notification()
		AppleScripts.execute_applescript(SCRIPT)
		print("Action Executed at")

x = 0
#while x is less than 2, complete the if loop
while x < 2:
	#if x is even execute the following 
	if x % 2 == 0:
		sniff(prn=execute_action, filter="arp", stop_filter=device_found)
		TIME = datetime.datetime.now()
		FORMATTED_TIME = TIME.strftime("%I:%M %p, %m/%d/%y")
		FIRST_COLUMN = TIME.strftime("%B %d, %Y")
		SECOND_COLUMN = TIME.strftime("%I:%M %p")
		thirdColumn = "Started Activity"
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, thirdColumn)
		print(" ")
		print("Started Activity")
		x += 1	
	#if x is not even execute the following
	else:
		sniff(prn=execute_action, filter="arp", stop_filter=device_found)
		TIME = datetime.datetime.now()
		FORMATTED_TIME = TIME.strftime("%I:%M %p, %m/%d/%y")
		FIRST_COLUMN = TIME.strftime("%B %d, %Y")
		SECOND_COLUMN = TIME.strftime("%I:%M %p")
		thirdColumn = "Ended Activity"
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, thirdColumn)
		print(" ")
		print("Ended Activity")
		x += 1
