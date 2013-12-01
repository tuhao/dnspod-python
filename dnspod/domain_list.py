# coding=utf-8
from dnspod_api import *
import sys

email = "astro.liuhang@gmail.com"
password = "njE_*8#j9"
domain_id = '10390973'
name = ['www.yasir.pw','yasir.pw']
record_id='47261432'
#record_id='47186219'
record_type='A'
record_line='默认'
value='114.92.148.141'
sub_domain='www'
ttl = '600'

def domain_list(email=email,password=password):
    try:
        api = DomainList(email=email, password=password)
        domain_list_txt = open('domain.txt', 'w')
        result = api().get("domains")
        result_str = str(result)
        domain_list_txt.write(result_str)
    except Exception, e:
        raise e
    finally:
        domain_list_txt.close()

def record_list(email=email,password=password,domain_id=domain_id):
	try:
		api = RecordList(email=email,password=password,domain_id=domain_id)
		record_list_txt = open('record.txt','w')
		for record in  api().get('records'):
			if record.get('type') == 'A':
				record_list_txt.write(str(record))
				#print record.get('value')
	except Exception, e:
		raise e
	finally:
		record_list_txt.close()




try:
	api = RecordModify(email=email,password=password,domain_id=domain_id,sub_domain=sub_domain,record_type=record_type, 
record_line=record_line, value=value,ttl=ttl,record_id=record_id)
	print api()
except Exception,e:
	raise e
finally:
	pass

#record_list(email, password, domain_id)

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


