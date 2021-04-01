import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


sqrt = []
for i in range(2,1000+1):
    sqrt.append(i**2)

t = int(input())

while t:
    t -= 1

    for num in sqrt:
        print(num)
        ans = input()
        if ans == '1':
            break
        else:
            continue

