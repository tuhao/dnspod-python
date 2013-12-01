#coding=utf-8
import time
import dnspod_tool
import ip

def modify():
	params = dict()
	try:
		conf = open('conf/dnspod.conf','r')
		for item in conf.readlines():
			temp = item.split('=')
			k = temp[0].strip()
			v = temp[1].strip()
			if ',' in v:
				v = v.split(',')
			params.update({k:v})
		pod = dnspod_tool.Dnspod_tool(**params)
		pod()
	except Exception, e:
		raise e
	finally:
		conf.close()

while True:
	last_ip = ip.get_from_local()
	
	time.sleep(1)
	print 'hi'
