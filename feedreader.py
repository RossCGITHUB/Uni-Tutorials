import feedparser
feeddata = feedparser.parse('http://www.reddit.com/r/python/.rss')

for post in feeddata.entries:
	
	print feeddata['entries'][0,5]['title'] + post.link + "\n"