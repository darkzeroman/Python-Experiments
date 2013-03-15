# Iterative Solution
arr = [5, -6, 7, 12, -3, 0, -11, -6]

T = []
max_value = 0

for index in range(len(arr)):
	if index == 0:
		T.append(arr[index])
	else:
		T.append(max([T[index-1] + arr[index], arr[index]]))

	max_value = max([max_value, T[index]])

print max_value