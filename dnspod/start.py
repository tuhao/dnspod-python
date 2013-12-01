#coding=utf-8
import sys
import time
from dnspod_fun import *

email = "astro.liuhang@gmail.com"
password = "njE_*8#j9"

domain_name_list = ['yasir.cn','yasir.pw']

record_type='A'
record_line='默认'
value='114.92.148.141'
ttl = '700'

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


domain_list_json = get_domain_list_json(email=email, password=password)
domain_ids = list()

for name in domain_name_list:
	domain_id = get_domain_id(name=name,domain_list_json=domain_list_json)
	domain_ids.append(domain_id)

pod = dict()
for domain_id in domain_ids:
	record_id_dict = get_record_id_dict(email=email,password=password,domain_id=domain_id)
	time.sleep(1)
	pod.update({domain_id:record_id_dict})

for domain_id in pod.keys():
	r_dict = pod.get(domain_id)
	for r_id in r_dict.keys():
		print modify_record(email=email,password=password,domain_id=domain_id,sub_domain=r_dict.get(r_id),record_type=record_type, 
record_line=record_line, value=value,ttl=ttl,record_id=r_id)
		time.sleep(2)
