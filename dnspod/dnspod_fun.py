# coding=utf-8
from dnspod_api import *


def get_domain_list_json(email, password):
    try:
        api = DomainList(email=email, password=password)
        return api().get("domains")
    except Exception, e:
        raise e


def get_domain_id(name, domain_list_json):
    for domain in domain_list_json:
        if domain.get('name') == name:
            return str(domain.get('id'))
    return str()


def get_record_id_dict(email, password, domain_id):
    record_dict = dict()
    try:
        api = RecordList(email=email, password=password, domain_id=domain_id)
        for record in api().get('records'):
            if record.get('type') == 'A':
                record_dict.update({str(record.get('id')):str(record.get('name'))})
    except Exception, e:
        raise e
    return record_dict


def modify_record(email, password, domain_id, sub_domain, record_type, record_line, value, ttl, record_id):
    try:
        api = RecordModify(
            email=email, password=password, domain_id=domain_id, sub_domain=sub_domain, record_type=record_type,
            record_line=record_line, value=value, ttl=ttl, record_id=record_id)
        return api().get('status')
    except Exception, e:
        raise e
