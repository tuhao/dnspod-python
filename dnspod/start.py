#coding=utf-8
import sys
from dnspod import *

params = dict()
try:
	conf = open('conf/dnspod.conf','r')
	for item in conf.readlines():
		params.update({item.split('=')[0].strip():str(item.split('=')[1].strip())})
	pod = Dnspod(params)
except Exception, e:
	raise e
finally:
	conf.close()

print params


if len(sys.argv) > 1:
	params = {'-e':'youremail@mail.com','-p':'yourpassword','-d':'yourdomain'}

	for arg in sys.argv:
		value = params.get(arg,None)
		if value:
			params.update({arg:value})
			#print arg + '  value:' + str(params.get(arg,None))
	print params
		
else:
	#print "Usege: python xxx.py -d yourdomain -e youremail -p yourpassword"
	pass

