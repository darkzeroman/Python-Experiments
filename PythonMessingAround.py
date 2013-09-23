class MyObject(object):
  foo = 1

  def test(self):
  	return 1

class MyMyObject(MyObject):

	def test(self):
		return 2


f = MyObject()
print f.test()

f = MyMyObject()
print f.test()
