import tweepy
import psutil
import datetime

CONSUMER_KEY = 'tJBneyDzhqCnac8RdrX4gGnMh'
CONSUMER_SECRET = 'gpx6Weoc8gWTI3lRwtLGGwvzCF2IQsOvrZt2YrRsCJ1A5dQf7L'
ACCESS_TOKEN = '4125858203-tN9kW5PKYGwWUFeDKpyGdKYMnAUb2SArlhJ3LBA'
ACCESS_TOKEN_SECRET = 'quEiAvhJSHXhDOLVt4rjoNpec4N1T6mTRLH3Nphqyjhxr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter = tweepy.API(auth)

max_allowed = 20
now = datetime.datetime.now()
last = datetime.datetime.now()

while True:
	cpu_percent = psutil.cpu_percent(interval = 1)
	now = datetime.datetime.now()
	if (now - last).total_seconds() > 300 :
		if cpu_percent > max_allowed:
			twitter.update_status(status= "Warning CPU percent currently: " + str(cpu_percent))
			last = datetime.datetime.now()
print ('done, exiting')
