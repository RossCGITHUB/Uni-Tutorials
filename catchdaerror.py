import urllib2 

req = urllib2.Request('http://www.rgu.ac.uk/test.php')

try: urllib2.urlopen(req)
except urllib2.HTTPError as e:
	code = e.code
	if code == 200:
		print "Shits all goood maan"

	elif code == 404:
		print "404 mate, no finding this"

	else:
		print "You've got an error"

except urllib2.URLError as e:
	print e.reason
else:
	print 'site is up'
	code = urllib2.urlopen(req).getcode()
	print code

