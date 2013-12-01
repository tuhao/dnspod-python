#coding=utf-8
from dnspod_fun import *
import time

class Dnspod():
 #email, password, domain_name_list, value, 
    def __init__(self,**kw):
        #self.email = email
        #self.password = password
        #self.domain_name_list = domain_name_list
        #self.value = value
        self.params = dict(
        	email='',password='',domain_name_list=list(),value='',
            record_type='A',
            record_line=u'默认',
            ttl='600'
        )
        self.params.update(kw)

    def modify():
        domain_list_json = get_domain_list_json(
            email=self.email, password=self.password)
        domain_ids = list()

        for name in self.domain_name_list:
            domain_id = get_domain_id(
                name=name, domain_list_json=domain_list_json)
            domain_ids.append(domain_id)

        pod = dict()
        for domain_id in domain_ids:
            record_id_dict = get_record_id_dict(
                email=self.email, password=self.password, domain_id=domain_id)
            time.sleep(1)
            pod.update({domain_id: record_id_dict})

        for domain_id in pod.keys():
            r_dict = pod.get(domain_id)
            for r_id in r_dict.keys():
                print modify_record(
                    email=self.email, password=self.password, domain_id=domain_id, sub_domain=r_dict.get(r_id), record_type=self.params['record_type'],
record_line=self.params['record_line'], value=self.value, ttl=self.params['ttl'], record_id=r_id)
                time.sleep(2)

    __call__ = modify
