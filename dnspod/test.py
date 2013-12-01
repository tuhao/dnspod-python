
class Test:
	def __init__(self,ip,**kw):
		self.name = 'sk'
		self.ip = ip
		self.params = dict(
			email='')
		self.params.update(kw)

	def show(self):
		print self.name + " " + self.ip
		print self.params
	__call__ = show

d = list()
d.append('abcd')
params = dict(
	{'email':'hi',
	'd':d})
test = Test('test',**params)
test()