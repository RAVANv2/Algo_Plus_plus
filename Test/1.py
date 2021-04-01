from collections import defaultdict

def sub_lists(l):
    base = []
    lists = [base]
    for i in range(len(l)):
        orig = lists[:]
        new = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new]
        lists = orig + lists

    return lists


# driver code
l1 = list(map(int,input().strip().split()))
b = int(input())

arr = sub_lists(l1)
ans = {}
ans = defaultdict(lambda :0,ans)
for ele in arr:
    if ele:
        if len(ele) == 1:
            ans[ele[0]] += 1
        else:
            num = 0
            for i in ele:
                num ^= i
            ans[num] += 1

sort_key = sorted(ans)
sum_ = 0
for i in sort_key:
    sum_ += ans[i]
    if sum_ > b:
        print(i)
        break
