# Finds the word that is the shortest repitition

def shortest_repitition(word):
  for i in range(1, len(word)/2 + 1):
    # print(i)
    if check_repitition(word, i):
      print word[:i]
      return
  print "No word"


def check_repitition(word, i):
  for j in range(i, len(word), i):
    if word[:i] != word[j:j+i]:
      return False
  return True

shortest_repitition("abcabcabc")

