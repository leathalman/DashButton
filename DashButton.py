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
THIRD_COLUMN = "Default Message"
SCRIPT = AppleScripts.SCRIPT
	
def device_found(packet_info):
	return DEVICE_MAC_ADDRESS == packet_info[ARP].hwsrc

def execute_action(packet_info, script=SCRIPT):
	if device_found(packet_info):
		AppNotification.send_notification()
		AppleScripts.execute_applescript(SCRIPT)

x = 0
while x < 2:
	if x % 2 == 0:
		sniff(prn=execute_action, filter="arp", stop_filter=device_found)
		CURRENT_TIME = datetime.datetime.now()
		#used to get the first time the button is pressed
		OLD_TIME = datetime.datetime.now()
		FORMATTED_TIME = CURRENT_TIME.strftime("%I:%M %p, %m/%d/%y")
		FIRST_COLUMN = CURRENT_TIME.strftime("%B %d, %Y")
		SECOND_COLUMN = CURRENT_TIME.strftime("%I:%M %p")
		THIRD_COLUMN = "Started Activity"
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, THIRD_COLUMN)
		print("Started Activity")
		print(" ")
		x += 1	
	elif x % 2 == 1:
		sniff(prn=execute_action, filter="arp", stop_filter=device_found)
		CURRENT_TIME = datetime.datetime.now()
		FORMATTED_TIME = CURRENT_TIME.strftime("%I:%M %p, %m/%d/%y")
		FIRST_COLUMN = CURRENT_TIME.strftime("%B %d, %Y")
		SECOND_COLUMN = CURRENT_TIME.strftime("%I:%M %p")
		#subtract the OLD_TIME from the first button press from the CURRENT_TIME of the second button press
		changeInTime = CURRENT_TIME - OLD_TIME
		#used to get the days, minutes, and second between the timedelta of the first and second button presses
		days = changeInTime.days
		hours, remainder = divmod(changeInTime.seconds, 3600)
		minutes, seconds = divmod(remainder, 60)
		THIRD_COLUMN = "Ended Activity, %r hours %r minutes" % (hours, minutes)
		GoogleSheets.add_row(FIRST_COLUMN, SECOND_COLUMN, THIRD_COLUMN)
		print("Ended Activity, %r hours %r minutes" % (hours, minutes))
		print(" ")
		x += 1
