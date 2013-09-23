import sys

def nextLine(paths, values):
  if len(values) == 1:
    return [update([], values[0])]

  nl = [update(paths[0], values[0])]

  for i in range(1, len(values)-1, 1):
    temp_1 = update(paths[i-1], values[i])
    temp_2 = update(paths[i], values[i])

    if temp_1[0] > temp_2[0]:
      nl.append(temp_1)
    else: 
      nl.append(temp_2)

  nl.append(update(paths[-1], values[-1]))
  return nl

def update(path, value):
  if len(path) == 0:
    path = [0, []]
  return [path[0] + value, [value] + path[1][:]]


# if len(sys.argv) >= 2:
#   test_cases = open(sys.argv[1], 'r')
# else:
#   test_cases = ["./triangle.txt"]
paths = []
for line in open(sys.argv[1], "r"):
  paths = nextLine(paths, map(int, line.rstrip().split(' ')))

all_paths = [path[0] for path in paths]
print max(all_paths)
    