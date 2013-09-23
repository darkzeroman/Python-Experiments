import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  f,b,n = map(int, test.split(' '))
  l = range(1,n+1,1)
  for index, item in enumerate(l):

    if ((item % f) + (item % b)) == 0:
      l[index] = "FB"
    elif (item % b) == 0:
      l[index] = "B"
    elif (item % f) == 0:
      l[index] = "F"
  print " ".join(map(str,l))
test_cases.close()