# DashButton
Use Python to enable actions with an Amazon Dash button.
 
 
# Setup
DashButton.py serves as the main file for interacting with the Dash Button. You need to replace 
```
DEVICE_MAC_ADDRESS = 'PUT MAC ADDRESS OF DASH BUTTON HERE' 
```
with the MAC address of your Dash Button. 

And in each of the module files (Applescript, AppNotification, etc.), the event name and secret key must be configured through IFTTT if you intend to use the Dash Button with that service. 
