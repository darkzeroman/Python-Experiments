import random

arr = [5, -6, 7, 12, -3, 0, -11, 3]

def quicksort(arr, low, high):

	if (high < low):
		return

	pivotindex= pivot(arr, low, high)

	quicksort(arr, low, pivotindex-1)
	quicksort(arr, pivotindex+1, high)

def swap(arr, first, second):
	arr[first], arr[second] = arr[second], arr[first]

def pivot(arr, low, high):
	pivotIndex = random.randint(low, high)
	swap(arr, pivotIndex, high)
	sortedindex = low

	for i in range(low, high):
		if arr[i] <= arr[high]:
			swap(arr, sortedindex, i)
			sortedindex+=1

	swap(arr, sortedindex, high)
	return sortedindex


quicksort(arr, 0, len(arr)-1)
print arr



