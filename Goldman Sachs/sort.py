def isSorted(arr):
	if len(arr) == 0 or len(arr) == 1:
		return True

	if (arr[0]<arr[1] and isSorted(arr[1:])):
		return True
	return False

arr = [1,2,3,4,5,6]

check = isSorted(arr)
print(check)