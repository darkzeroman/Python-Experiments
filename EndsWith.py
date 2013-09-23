import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if not test:
    continue
  first, second = test.split(',')
  if len(second) > len(first):
    print(0)
    continue

  if first[len(first) - len(second):len(first)] == second:
    print(1)
  else:
    print(0)

test_cases.close()

# test_cases = ["Hello World,World", "Hello CodeEval,CodeEval", "San Francisco,San Jose"]