#coding=utf-8
import time
import pod
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


#wan_ip = ip.get_from_local()
wan_ip = ip.get()
print 'now ip : ' +  wan_ip
params = init_params()
instance = pod.dnspod(**params)
record_list = instance.get_records()

need_modify = list()
for record in record_list:
	if record.value != wan_ip:
		need_modify.append(record)

instance.modify(record_list=need_modify,value=wan_ip)

print 'done,start to monitor work' 

while True:
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' ' + wan_ip
	#now_ip = ip.get_from_local()
	now_ip = ip.get()
	if wan_ip != now_ip:
		print wan_ip + ' is outdate,' 
		print 'now wan ip is ' + now_ip 
		print 'modify begin at ' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		instance.modify(record_list=instance.get_records(),value=now_ip)
		wan_ip = now_ip
	time.sleep(60)
