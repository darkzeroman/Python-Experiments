class MyClass(object):
	def __init__(self):
		print "called in this case"
	def __str__(self):
		return "test"

obj = MyClass()
print obj

print str(obj)
print repr(obj)

test()

def test():
	print("lol")

