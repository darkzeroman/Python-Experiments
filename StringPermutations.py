import sys

final_list = []

def recCall(word, word_bool, curr_word):
  if len(curr_word) == len(word_bool):
    final_list.append("".join(curr_word))
    return

  for index, item in enumerate(word_bool):
    if not item:
      word_bool[index] = True
      curr_word.append(word[index])
      recCall(word, word_bool, curr_word)
      word_bool[index] = False
      curr_word.pop()


test_cases = open(sys.argv[1], 'r')
# test_cases = ["hat", "", "abc"]
for test in test_cases:
  if len(test)==0:
    continue
  final_list = []
  test = test.rstrip()
  recCall(list(test), [False]*len(test), [])
  print ",".join(sorted(final_list))

test_cases.close()