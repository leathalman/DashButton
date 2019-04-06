#!/usr/bin/python
from subprocess import Popen, PIPE

WAKEUP_SCRIPT = '''
	tell application "Safari"
		tell window 1
			set current tab to (make new tab with properties {URL:"http://www.stackoverflow.com"})
		end tell
	end tell
	'''

def execute_applescript(packet_info, script=WAKEUP_SCRIPT):
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE)
	p.communicate(script)
	print("Action Executed")

#execute_applescript(WAKEUP_SCRIPT)