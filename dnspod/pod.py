# coding=utf-8
import podmodel
import time


class dnspod:

    def get_records(self):
            domain_id_list = self.get_domains()
            record_list = self.get_record_list(domain_id_list)
            return record_list

    def get_domains(self):
            domain_id_list = list()
            domain_list = podmodel.domains(
                email=self.email, password=self.password)
            for domain in domain_list:
                for name in self.domain_name:
                    if domain.name == name:
                        domain_id_list.append(domain.id)
            return domain_id_list

    def get_record_list(self, domain_id_list):
            record_list = list()
            for domain_id in domain_id_list:
                for item in podmodel.records(email=self.email, password=self.password, domain_id=domain_id):
                    record_list.append(item)
                time.sleep(1)
            return record_list

    def modify(self, record_list, value, **kw):
            if record_list and len(record_list) > 0:
                for record in record_list:
                    print podmodel.modify_record(
                        email=self.email, password=self.password, domain_id=record.domain_id, sub_domain=record.name, record_type=self.params[
                            'record_type'], record_line=self.params['record_line'], value=value, ttl=self.ttl, record_id=record.id)
                    time.sleep(1)

    def __init__(self, email, password, domain_name,ttl, **kw):
        self.email = email
        self.password = password
        self.domain_name = domain_name
        self.ttl = ttl
        self.params = dict(
            record_type='A',
            record_line=u'默认'.encode('utf-8')
        )
        self.params.update(kw)
