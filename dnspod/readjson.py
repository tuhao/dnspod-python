#coding=utf-8
import json
name = 'yasir.pw'
try:
	text = open('domain.txt','r')
	#json = eval(text.read())
	json_object = eval(text.read())
	for record in json_object:
		if record.get('name') == name:
			print record.get('id')
		
except Exception, e:
	raise e
finally:
	text.close()