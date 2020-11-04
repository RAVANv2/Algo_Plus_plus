
def merge(a,s,e):
	i = s
	mid = (s+e)//2
	j = mid+1
	k = s
	temp = [0]*(len(a)+1)

	count = 0
	while i<=mid and j<=e:
		if a[i] <= a[j]:
			temp[k] = a[i]
			i+=1
			k+=1
		else:
			temp[k] = a[j]
			count += mid - i + 1
			for l in range(i,mid+1):
				pair.add((a[i],a[j]))

			k+=1
			j+=1
	while i<=mid:
		temp[k] = a[i]
		k+=1
		i+=1

	while j<=e:
		temp[k] = a[j]
		k+=1
		j+=1

	for n in range(s,e+1):
		a[n] = temp[n] 

	return count

def inversion_count(a,s,e):
	if s>=e:
		return 0

	mid = (s+e)//2
	x = inversion_count(a,s,mid)
	y = inversion_count(a,mid+1,e)
	z = merge(a,s,e)

	return x+y+z

a = [1,5,2,6,3,0]
pair = set()
print(inversion_count(a,0,len(a)-1))
print(pair)
print(a)