# a b c d 4
# e f g h 2

import sys
# test_cases = ["a b c d 4", "e f g h 2"]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    str_list = test.split(' ')
    temp_index = int(str_list[len(str_list) - 1])

    real_index = len(str_list) - 1 - temp_index

    if real_index < 0 or real_index >= len(str_list):
      continue
    else:
      print str_list[real_index]
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()