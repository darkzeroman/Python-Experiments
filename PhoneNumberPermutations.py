from datetime import datetime
startTime = datetime.now()


numbers_letters = {2: list("abc"), 3: list("def"), 4: list("ghi"), 
5: list("jkl"), 6: list("mno"), 7: list("pqrs"), 8: list("tuv"), 9: list("wxyz")}


def phone_number_perms(index=0, phone_str=None):
	if phone_str is None:
		phone_str = ""
	if index == len(phone_num):
		print phone_str
		return

	digit = int(phone_num[index])

	if numbers_letters.has_key(digit):
		for c in numbers_letters[digit]:
			phone_number_perms(index+1, phone_str+c)
	else:
		phone_number_perms(index+1, phone_str+str(digit))

phone_num = list("7705791412")

phone_number_perms()

print(datetime.now()-startTime)
