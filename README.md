# DashButton
Use Python to enable actions with an Amazon Dash button.


# Setup
DashButton.py serves as the main file for interacting with the Dash Button.
You need to **replace** the below text with the MAC address of your Dash Button.

```
DEVICE_MAC_ADDRESS = 'PUT MAC ADDRESS OF DASH BUTTON HERE'
```

In each of the module files (Applescript, AppNotification, etc.), the event name and secret key must be configured through IFTTT if you intend to use the Dash Button with that service.

```
requests.post("https://maker.ifttt.com/trigger/button_pressed/with/key/PLACEHOLDER")
```

```button_pressed``` refers to the event name in IFTTT and ```PLACEHOLDER``` is the secret key created with [webooks](https://ifttt.com/services/maker_webhooks/settings) in IFTTT.


# Functionality
With the three default modules to DashButton.py, the script will send a notification to your phone, log the start and end times for an activity, and open a new tab in Safari on each button press. This can be configured to your preference easily.

Contact me if you have any questions, I will be adding functionality as I go.
