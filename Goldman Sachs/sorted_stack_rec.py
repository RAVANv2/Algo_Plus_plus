
def insert(arr,ele):
	if len(arr) == 0 or ele > arr[-1]:
		arr.append(ele)
	else:
		temp = arr.pop()
		insert(arr,ele)
		arr.append(temp)


def sorted(arr):
	if len(arr):
		temp = arr.pop()
		sorted(arr)
		insert(arr,temp)

arr = [-3,14,18,-5,30]
sorted(arr)
for _ in range(len(arr)):
	print(arr.pop(),end=' ')
