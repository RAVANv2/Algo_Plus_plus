
def buidTree(arr,lvl):
    if len(arr)<=0:
        return
    index = arr.index(max(arr))
    ans[arr[index]] = lvl
    buidTree(arr[:index],lvl+1)
    buidTree(arr[index+1:],lvl+1)

t = int(input())

for _ in range(t):
    n = int(input());arr = list(map(int,input().strip().split()))
    ans = {}
    for key in arr: ans[key] = 0
    buidTree(arr,0);print(*ans.values())
