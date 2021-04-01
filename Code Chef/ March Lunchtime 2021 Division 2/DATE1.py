import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1
    a,y,x = list(map(int,input().strip().split()))

    count = 1
    size = y
    while a>=0:
        if size == 0:
            count -= 1
            size = y
        a -= x
        size -= 1
        count += 1
    print(count)