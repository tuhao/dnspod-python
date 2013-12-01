import json
class Test:

    def __init__(self, name, **kw):
        self.name = name
        #self.ip = ip
        #self.params = dict(
         #   email='')
        #self.params.update(kw)

    def show(self):
        print self.name  # + " " + self.ip
       # print self.params
    __call__ = show

#d = list()
#d.append('abcd')
#params = dict({'email': 'hi', 'name': 'yasir','d': d,'what':'what'})
#test = Test(**params)
#test()

class Record:

    def __init__(self,id,name,value,domain_id=-1,**kw):
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

    def modify(self,record_list,**kw):
    	if record_list:
    		print record_list
    	else:
    		print 'Not exits!'

    def next(self,record_list):
        if record_list:
            print record_list
        else:
            print 'Not exits!'

params = dict(id='1',name='hi',status='enable')
domain = Domain(**params)
domain.next(None)
#text = open('record.txt','r')
#records = eval(text.read())
##print records.get('records')
#result = list()
#for item in records.get('records'):
#	if item.get('type') == 'A':
#		 params = dict(item)
#		 print params
#		 result.append(Record(**params))
#text.close()
#print result[0].params

#result = list()
#text = open('domain.txt','r')
#domains = eval(text.read())
#for item in domains.get('domains'):
#	params = dict(item)
#	result.append(Domain(**params))
#	#print item
#text.close()
#record_lis = ['hi']
#result[0].modify(record_lis)



