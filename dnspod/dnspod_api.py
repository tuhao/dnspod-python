# coding=utf-8
import urllib
import httplib
import re
import json


class ApiCn:

    def __init__(self, email, password, **kw):
        self.base_url = "dnsapi.cn"
        self.params = dict(
            login_email=email,
            login_password=password,
            format="json",
        )
        self.params.update(kw)
        self.path = None

    def request(self, **kw):
        self.params.update(kw)
        if not self.path:
            """Class UserInfo will auto request path /User.Info."""
            name = re.sub(r'([A-Z])', r'.\1', self.__class__.__name__)
            self.path = "/" + name[1:]
        conn = httplib.HTTPSConnection(self.base_url)
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept":
                   "text/json", "User-Agent": "dnspod-python/0.01 (im@chuangbo.li; DNSPod.CN API v2.8)"}
        conn.request("POST", self.path, urllib.urlencode(self.params), headers)

        response = conn.getresponse()
        data = response.read()
        conn.close()
        ret = json.loads(data)
        if ret.get("status", {}).get("code") == "1":
            return ret
        else:
            raise Exception(ret)

    __call__ = request


class _DomainApiBase(ApiCn):

    def __init__(self, domain_id, **kw):
        kw.update(dict(domain_id=domain_id))
        ApiCn.__init__(self, **kw)


class RecordCreate(_DomainApiBase):

    def __init__(self, sub_domain, record_type, record_line, value, ttl, mx=None, **kw):
        kw.update(dict(
            sub_domain=sub_domain,
            record_type=record_type,
            record_line=record_line,
            value=value,
            ttl=ttl,
        ))
        if mx:
            kw.update(dict(mx=mx))
        _DomainApiBase.__init__(self, **kw)


class RecordModify(RecordCreate):

    def __init__(self, record_id, **kw):
        kw.update(dict(record_id=record_id))
        RecordCreate.__init__(self, **kw)


class DomainList(ApiCn):
    pass


class RecordList(_DomainApiBase):
    pass
