import tweepy

CONSUMER_KEY = 'tJBneyDzhqCnac8RdrX4gGnMh'
CONSUMER_SECRET = 'gpx6Weoc8gWTI3lRwtLGGwvzCF2IQsOvrZt2YrRsCJ1A5dQf7L'
ACCESS_TOKEN = '4125858203-tN9kW5PKYGwWUFeDKpyGdKYMnAUb2SArlhJ3LBA'
ACCESS =_TOKEN_SECRET = 'quEiAvhJSHXhDOLVt4rjoNpec4N1T6mTRLH3Nphqyjhxr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter = tweepy.API(auth)

twitter.update_status(status = 'hello world')

print ('done, exiting')
