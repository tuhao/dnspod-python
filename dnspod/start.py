#coding=utf-8
import sys

if len(sys.argv) > 1:
	params = {'-e':'youremail@mail.com','-p':'yourpassword','-d':'yourdomain'}

	for arg in sys.argv:
		value = params.get(arg,None)
		if value:
			params.update({arg:value})
			#print arg + '  value:' + str(params.get(arg,None))
	print params
		
else:
	print "Usege: python xxx.py -d yourdomain -e youremail -p yourpassword"