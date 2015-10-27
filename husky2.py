import urllib2

req = urllib2.Request('http://my.pretend.server')

response = urllib2.urlopen(req)

the_page = response.read()