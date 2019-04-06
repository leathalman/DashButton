#scapy needed to discover and recieve signal from Dash Button
from scapy.all import *
#Popen needed for applescipt integration in Python
from subprocess import Popen, PIPE
#Requests used for webhooks with IFTTT
import requests
import datetime
import GoogleSheets
import AppNotification
import AppleScripts

#Static var for the MAC Address of Dash Button beacuse I'm lazy
DEVICE_MAC_ADDRESS = 'PUT MAC ADDRESS OF DASH BUTTON HERE'
TIME = datetime.datetime.now()
FORMATTED_TIME = TIME.strftime("%I:%M %p, %m/%d/%y")
FIRST_COLUMN = TIME.strftime("%B %d, %Y")
SECOND_COLUMN = TIME.strftime("%I:%M %p")
thirdColumn = "Default Message"
	
def device_found(packet_info):
	return DEVICE_MAC_ADDRESS == packet_info[ARP].hwsrc

def execute_action(packet_info):
	if device_found(packet_info):
		AppNotification.send_notification()
		AppleScripts.execute_applescript(WAKEUP_SCRIPT)
		print("Action Executed at %r" %FORMATTED_TIME)

x = 0
while x < 2:
	if x % 2 == 0:
		sniff(prn = execute_action, filter="arp")
		thirdColumn = "Started Activity"
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, thirdColumn)
		print("Started Activity")
		x += 1	
	else:
		sniff(prn = execute_action, filter="arp", stop_filter=device_found)
		thirdColumn = "Ended Activity"
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, thirdColumn)
		print("Ended Activity")
		x += 1
