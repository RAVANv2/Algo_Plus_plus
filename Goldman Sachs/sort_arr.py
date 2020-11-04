

def sort_arr(arr,n):
	if n==1:
		return

	for i in range(n-1):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
	sort_arr(arr,n-1)

def reverse_prefix(arr):
	new_arr = [None for _ in range(len(arr))]
	new_arr[0] = arr[0]
	for i in range(1,len(arr)):
		new_arr[i] = arr[i] + new_arr[i-1]
	return new_arr


if __name__ == "__main__":
	arr = [6,3,1,7,9,2]
	sort_arr(arr,len(arr))
	new_arr = reverse_prefix(arr)
	print(new_arr)
	print(arr)