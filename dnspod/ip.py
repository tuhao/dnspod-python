
import urllib2
import re

def find_ip(content):
	pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
	return pattern.search(content).group(0)

def get():
	try:
		content = urllib2.urlopen('http://iframe.ip138.com/ic.asp').read()
		return find_ip(content)
	except Exception, e:
		raise e

#print get_ip()

import base64

def get_from_local():
	url = 'http://192.168.0.1/info.htm'
	auth = base64.encodestring('admin:504504')
	headers = {'Authorization':"Basic " + auth}
	try:
		req = urllib2.Request(url, None, headers)
		response = urllib2.urlopen(req)
		return response.read()
	except Exception, e:
		raise e

print find_ip(get_from_local())