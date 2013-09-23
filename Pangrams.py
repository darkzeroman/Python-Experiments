import sys
import string

# test_cases = ["A quick brown fox jumps over the lazy dog", "A slow yellow fox crawls under the proactive dog", ""]
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  not_seen_letters = dict(zip(list(string.lowercase), [True]*26))

  for k in list(string.lower(test)):
    if not_seen_letters.has_key(k):
      del not_seen_letters[k]

  if len(not_seen_letters) == 0:
    print "NULL"
  else:
    print "".join(sorted(not_seen_letters.keys()))
      
test_cases.close()