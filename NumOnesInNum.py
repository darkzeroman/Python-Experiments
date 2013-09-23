def numOnes(num):
  count = 0
  one = 1
  for i in range(32):
    if (num & one):
      count += 1
    one = one << 1
  print(count)



numOnes(65)