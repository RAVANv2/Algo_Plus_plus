import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def factors(n):
    return len(set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup))
new_dic = {}
for i in range(1,100000+1):
    new_dic[i] = factors(i)

n = int(input())

arr = list(map(int,input().split()))

for ele in arr:
    if new_dic[ele] == 3:
        print("YES")
    else:
        print("NO")