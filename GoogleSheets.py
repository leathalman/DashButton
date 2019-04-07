import requests
import datetime

time = datetime.datetime.now()
formattedTime = time.strftime("%B %d, %Y")
startTime = time.strftime("%I:%M %p")

def add_row(first, second, third):
	report = {}
	report["value1"] = first
	report["value2"] = second
	report["value3"] = third
	#will call IFTTT event for google sheets with 3 values
	requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/PLACEHOLDER", data=report) 
	print("GoogleSheets Executed")

#firstColumn = formattedTime
#secondColumn = startTime
#thirdColumn = "Message"

#add_row(firstColumn, secondColumn, thirdColumn)
