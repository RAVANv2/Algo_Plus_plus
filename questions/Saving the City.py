import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

t = int(input())
while t:
    t -= 1
    a,b = list(map(int,input().split()))
    s = input()

    count = float("inf")
    ans = 0
    for char in range(len(s)):
        if s[char] == "0":
            count += 1
        else:
            ans += min(a,b*count)
            count = 0

    print(ans)


