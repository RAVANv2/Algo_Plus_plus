


arr = [3,10,2,1,20]

lis = [1]*len(arr)

max_ = float("-inf")

for i in range(1,len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            lis[i] = max(lis[i],lis[j]+1)
            max_ = max(lis[i],max_)

print(max_)
print(lis)