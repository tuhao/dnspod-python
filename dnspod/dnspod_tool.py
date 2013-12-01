# coding=utf-8

import time
from dnspod_fun import *

class Dnspod_dict_tool:

    def __init__(self, email, password, domain_name_list, value, **kw):
        self.email = email
        self.password = password
        self.domain_name_list = domain_name_list
        self.value = value

        self.params = dict(
            record_type='A',
            record_line=u'默认'.encode('utf-8'),
            ttl='600'
        )
        self.params.update(kw)

    def modify(self,m_params,**kw):
        if m_params:
            pass
        else:
            domain_id_list = get_domain_id_list(self)
            record_list = get_record_list(self,domain_id_list)
        for record in record_list:
            print modify_record(email=self.email, password=self.password, domain_id=record.domain_id, sub_domain=record.name, record_type=self.params['record_type'],
record_line=self.params['record_line'], value=self.value, ttl=self.params['ttl'], record_id=record.id)
            time.sleep(1)


#    def ip_val(self,wan_ip):
#        domain_id_list = get_domain_id_list(self)
#        record_ip_dict = get_record_ip_dict(email=self.email, password=self.password, domain_id=domain_id)
#        params = dict()
#        for k in record_ip_dict.keys():
#            if record_ip_dict.get(k) != wan_ip:
#                params.update({k:})


    def get_domain_id_list(self):
        domain_id_list = list()
        domain_list = domains(email=email,password=password)
        for domain in domain_list:
            for name in self.domain_name_list:
                if domain.name == name:
                    domain_id_list.append(domain.id)
        return domain_id_list

    def get_record_list(self,domain_id_list):
        record_list = list()
        for domain_id in domain_id_list:
            record_list = records(email=self.email, password=self.password, domain_id=domain_id)
            time.sleep(1)
        return record_list
    
