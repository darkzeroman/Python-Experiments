def recCall(arr, index, curr_arr):
  if len(curr_arr) == 4:
    if reduce(lambda x,y: x+y, curr_arr) == 0:
      return 1
    else:
      return 0
  
  if index >= len(arr):
    return 0

  sum = recCall(arr, index+1, curr_arr + [arr[index]])
  sum += recCall(arr, index+1, curr_arr[:])
  
  return sum

test_cases = [[2,3,1,0,-4,-1],[0,-1,3,-2]]
# test_cases = [[2,3,1,0,5]]
for test in test_cases:
  print recCall(test, 0, [])
