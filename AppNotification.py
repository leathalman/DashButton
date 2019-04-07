import requests

#Example for simple IFTTT webhook call

def send_notification():
	#will call IFTTT event for App Notification
	#button_pressed is the "Event Name"
	#"PLACEHOLDER" is the "Secret Key" from IFTTT
	requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/PLACEHOLDER")
	print("AppNotification Executed")

#will send a notification reading "Amazon Button pressed!" as configured by IFTTT
#send_notification()
