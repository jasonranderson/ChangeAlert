#!/usr/bin/env python
# encoding: utf-8

"""
ChangeAlert.py

Created by Jason Anderson on 2013-04-19.
Copyright (c) 2013 Kosoku Interactive, LLC. All rights reserved.
"""

import sys
import time
import os.path
import pickle
import urllib2
import twilio

request = urllib2.Request('path/to/webpage/in/question/')
compare_file = '/path/to/last/saved/version/of/webpage/compare_html.p'
log_file = '/path/to/log/file/log.txt'
response = urllib2.urlopen(request) # Make the request
htmlString = response.read()

account_sid = "twilio_account_sid"
auth_token  = "twilio_account_token"

try: 
    file = pickle.load( open( compare_file, 'rb'))
    if pickle.load( open( compare_file, 'rb')) == htmlString:
		localtime = time.asctime( time.localtime(time.time()) )
		f = open(log_file,'a')
		f.write(localtime + '\n\r')
		sys.exit(0)
    else:
        pickle.dump( htmlString, open( compare_file, "wb" ) )

 	try:
		from twilio.rest import TwilioRestClient
		client = twilio.rest.TwilioRestClient(account_sid, auth_token)

		message = client.sms.messages.create(
			body="Set the body of your text message here...",
			to="+1234567890", #number to send SMS message to
			from_="+1234567890" #twilio number message is coming from
		)

	except twilio.TwilioRestException as e:
		print e

except IOError: 
    pickle.dump( htmlString, open( compare_file, "wb" ) )
