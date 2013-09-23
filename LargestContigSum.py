def naive(arr):
  max_arr = []
  max_sum = -99999

  for i in range(len(arr)):
    for  j in range(i+1, len(arr) ):
      print arr[i:j]
      t_sum = reduce(lambda x,y: x+y, arr[i:j])
      if t_sum > max_sum:
        max_sum = t_sum
        max_arr = arr[i:j]
  print max_arr

naive([1,2,3,-1000, 100])
# print "test"

