n,s = list(map(int,input().strip().split()))
left = 0
right = 0
sum = 0
a = []
for i in range(0,n):
    temp = int(input())
    a.append(temp)

num = 0
for i in range(0,n):
    right += 1
    sum += a[i]
    while sum > s:
        sum -= a[left]
        left += 1
    num += right - left

den = (n+1)*(n)//2


ans = 1.0*num/den
print(round(ans,8))

