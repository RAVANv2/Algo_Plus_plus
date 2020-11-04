
def binary_search(arr,key):
	s = 0
	end = len(arr)-1
	while s <= end:
		mid = (s+end)//2

		if arr[mid] == key:
			return mid

		if arr[mid] > key:
			end = mid - 1
		else:
			s = mid + 1

	return -1


arr = [1,2,3,4,5,6,7]
key = 7
print(binary_search(arr,key))