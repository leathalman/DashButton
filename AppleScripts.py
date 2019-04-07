#!/usr/bin/python
from subprocess import Popen, PIPE

#any url can be replaced in the quotes below, I use google sheets as default
SCRIPT = '''
	tell application "Safari"
		tell window 1
			set current tab to (make new tab with properties {URL:"https://docs.google.com/spreadsheets/d/1fRhHG70r7nnoCD7CR0iObUyjg_oR_6ZAzPFh04Z-6Rs/edit#gid=0"})
		end tell
	end tell
	'''

def execute_applescript(packet_info, script=SCRIPT):
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
	p.communicate(script)
	print("AppleScript Executed")

#execute_applescript(SCRIPT)
