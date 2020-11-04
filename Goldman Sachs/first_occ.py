def all_occ(arr,key,i):
	if i==len(arr):
		return

	if arr[i] == key:
		ans.append(i)

	all_occ(arr,key,i+1)

def last_occ(arr,key):

	if len(arr) == 0:
		return -1

	ans = last_occ(arr[1:],key)

	if ans == -1:
		if arr[0] == key:
			return 0
		else:
			return -1

	return ans+1

def first_occ(arr,key):
	if len(arr) == 0:
		return -1

	if arr[0] == key:
		return 0 

	ans = first_occ(arr[1:],key)
	if ans == -1:
		return -1
	return ans+1



arr = [1,2,3,7,4,5,7,10]
key = 7
print(first_occ(arr,key))
print(last_occ(arr,key))
ans = []
all_occ(arr,key,0)
print(ans)