import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def factors(n):
    return len(set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup))

new_dic = {}
for i in range(1,100000):
    new_dic[i] = factors(i)

arr = list(map(int,input().strip().split()))
ans = []
for num in arr:
    new = num
    while new_dic[new] != 9:
        new += 1
    ans.append(new)
print(ans)
