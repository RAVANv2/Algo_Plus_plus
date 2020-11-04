def merge(a,s,e):
	mid = (s+e)//2
	i = s
	j = mid+1
	k = s
	temp=[0]*(len(a)+1)

	while i<=mid and j<=e:
		if a[i] < a[j]:
			temp[k] = a[i]
			i += 1
			k += 1
		else:
			temp[k] = a[j]
			k += 1
			j += 1

	while i<=mid:
		temp[k] = a[i]
		k += 1
		i += 1
	while j<=e:
		temp[k] = a[j]
		k += 1
		j += 1
	for _ in range(s,e+1):
		a[_] = temp[_] 


def merge_sort(a,s,e):
	if s >= e:
		return
	mid = (s+e)//2
	merge_sort(a,s,mid)
	merge_sort(a,mid+1,e)
	merge(a,s,e)

a = [1,3,4,2,9,6,7]
merge_sort(a,0,len(a)-1)
print(a)