
n,days = input().split()
arr = list(map(int,input().strip().split()))
ind = []

for i in range(len(arr)):
    ind.append([i+1,arr[i]])
ans = 0
for ele in ind:
    ans += abs(ele[0] - ele[1])

if ans < int(days):
    print("Yes",ans)
else:
    print("No")
