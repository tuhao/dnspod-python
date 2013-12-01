# coding=utf-8
from dnspod_api import *


class Record:

    def __init__(self,domain_id,id,name,value,**kw):
        self.domain_id = domain_id
        self.id = id
        self.name = name
        self.value = value
        self.params = dict()
        self.params.update(kw)

class Domain:

    def __init__(self,id,name,status,**kw):
        self.id = id
        self.name = name
        self.status = status
        self.params = dict()
        self.params.update(kw)



def get_domains_json(email, password):
    api = DomainList(email=email, password=password)
    return api().get("domains")

def get_records_json(email,password,domain_id):
    api = RecordList(email=email, password=password, domain_id=domain_id)
    return api().get('records')

def domains(email,password):
    domain_list = list()
    domain_json = get_domains_json(email=email,password=password)
    for doamin in domain_json:
        params = dict(domain)
        domain_list.append(**params)
    return domain_list

def records(email, password, domain_id):
    record_list = list()
    records_json = get_records_json(email=email,password=password, domain_id=domain_id)
    for record in records_json:
        if record.get('type') == 'A':
            params = dict(record)
            record_list.append(Record(domain_id=domain_id,**params))
    return record_list


def modify_record(email, password, domain_id, sub_domain, record_type, record_line, value, ttl, record_id):
    api = RecordModify(
        email=email, password=password, domain_id=domain_id, sub_domain=sub_domain, record_type=record_type,
        record_line=record_line, value=value, ttl=ttl, record_id=record_id)
    return api().get('status')
