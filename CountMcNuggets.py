
packages = [6,9,20]


def mc(n):
	if n < 0:
		return False

	if n in packages:
		return True

	for package in packages:
		if mc(n-package):
			return True
	
	return False


print mc(60)