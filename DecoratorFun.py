def firstDec(fn):
	def wrapped():
		return "firstDec " + fn() + " firstDec"
	return wrapped;

def secondDec(fn):
	def wrapped():
		return "secondDec " + fn() + " secondDec"
	return wrapped;

@firstDec
@secondDec
def test():
	return "hello world"


print test()
