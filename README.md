ChangeAlert
===========

This script checks the contents of a specific URL and writes the HTML to a local file.

Subsequent checks of the URL compare the resulting HTML with the HTML in the local file to see if changes have been made.

If changes are detected, the script sends an SMS message to the selected number via the Twilio (http://twilio.com) web service.