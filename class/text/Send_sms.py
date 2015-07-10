##send_sms.py
# this para i was trying to connect office ip
'''import urllib2
proxy_support = urllib2.ProxyHandler({"http":"http://10.7.81.4:8080"})
opener = urllib2.build_opener(proxy_support)
#urllib2.install_opener(opener)'''


from twilio.rest import TwilioRestClient
 
#Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4838910cdccbb3c817c75c69c8cfcd84"
auth_token  = "e1b62f7480097842c294d9fe6323ee0c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="This is awesome",
    to="+919777450599",    # Replace with your phone number
    from_="+19713024440") # Replace with your Twilio number
print message.sid
