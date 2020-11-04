def fast_bubble_sort(arr,s,n):
	if n==1:
		return
	if s == n-1:
		fast_bubble_sort(arr,0,n-1)

	if arr[s]>arr[s+1]:
		arr[s],arr[s+1] = arr[s+1],arr[s]
	fast_bubble_sort(arr,s+1,n)





def bubble_sort(arr,n):
	if n == 1:
		return

	for i in range(n-1):
		if arr[i] > arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]


	bubble_sort(arr,n-1)



arr = [1,3,5,4,2]
# bubble_sort(arr,len(arr))
fast_bubble_sort(arr,0,len(arr)-1)
print(arr)