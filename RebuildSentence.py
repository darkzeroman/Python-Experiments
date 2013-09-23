d = set(["my", "name", "is", "bob", "together","to", "get", "her", "good", "goo", "d", "go", "od"])

def rebuild(curr_str, path):
	if not len(curr_str):
		print path

	for i in range(len(curr_str)+1):
		if curr_str[:i] in d:
			new_path = list(path)
			new_path.append(curr_str[:i])
			rebuild(curr_str[i:], new_path)

rebuild("mynameisbob",[])
rebuild("good",[])