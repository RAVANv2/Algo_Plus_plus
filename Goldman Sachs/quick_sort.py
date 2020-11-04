def partition(a,s,e):
	pivot = a[e]
	i = s-1
	
	for j in range(s,e):
		if a[j] <= pivot:
			i += 1
			a[i],a[j] = a[j],a[i]
	i += 1
	a[i],a[e] = a[e],a[i]
	return i


def quick_sort(a,s,e):
	if s >= e:
		return

	p = partition(a,s,e)

	quick_sort(a,s,p-1)
	quick_sort(a,p+1,e)

a = [1,7,8,9,5,6,4]
quick_sort(a,0,len(a)-1)
print(a)