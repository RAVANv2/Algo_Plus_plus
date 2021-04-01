


arr = [1,0,2,3,0,4,5,0]

i = 0
n = len(arr)
while i < n:
    if arr[i] == 0:
        arr.insert(i,0)
        i += 2
    else:
        i += 1

del arr[n:]
print(arr)