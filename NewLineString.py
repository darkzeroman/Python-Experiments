import sys

input_str = "ABCXYZACCD"


temp_word = ""
for index in range(len(input_str)):
  curr_char = input_str[index]

  if len(temp_word) == 0:
    temp_word += curr_char
    continue

  if len(temp_word) and (ord(temp_word[-1]) + 1 == ord(curr_char)):
    temp_word += curr_char
  else:
    print(temp_word)
    temp_word = ""
    temp_word += curr_char

print(temp_word)


print "\nTry two\n"

for index in range(len(input_str)):
  if index == 0:
    sys.stdout.write(input_str[index])
    continue

  if ord(input_str[index-1]) + 1 == ord(input_str[index]):
    sys.stdout.write(input_str[index])
  else:
    print('')
    sys.stdout.write(input_str[index])

print