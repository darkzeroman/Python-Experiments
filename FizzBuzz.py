

for i in range(1,16):
	if not (i % 3 or i % 5):
		msg = "FizzBuzz"
	elif not i % 3:
		msg = "Fizz"
	elif not i % 5:
		msg = "Buzz"
	else:
		msg = i
	print msg


def fn(x):
	
	return 


print [fn(x) for x in range(1,16)]