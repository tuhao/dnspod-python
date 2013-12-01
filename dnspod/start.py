#coding=utf-8
import time
import dnspod_tool
import ip

def init_params():
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
		return params
	except Exception, e:
		raise e
	finally:
		conf.close()

params = init_params()
pod = dnspod_tool.Dnspod_tool(**params)

wan_ip = ip.get_from_local()


m_params = dict({})
pod.modify(m_params)

while True:

	now_ip = ip.get_from_local()

	time.sleep(1)
	print 'hi'

