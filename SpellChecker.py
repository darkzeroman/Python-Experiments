import itertools

vowels = "aeiou"
# cat => [["c"], ["a","e", "i", "o", "u"], ["t"]]
def generate_vowel_perms(word):
	l = [list(vowels) if char in vowels else list(char) for char in word]
	return ["".join(r) for r in itertools.product(*l)]

def spellchecker(word):
	word = word.lower()
	if not spellchecker_helper(word):
		print "NO SUGGESTIONS"


def spellchecker_helper(word):
	l = list()
	l.append(word)
	l.extend(generate_vowel_perms(word))
	# print l
	if test_words(l):
		return True

	# find repeated letters and shorten them
	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			if spellchecker_helper(word[:i] + word[i+1:]):
				return True
	return False

def test_words(word_list):
	dictionary_set = set(["sheep"]) # load dictionary here
	for word in word_list:
		if word in dictionary_set:
			print word
			return True
	return False

spellchecker("sheeeppp")
