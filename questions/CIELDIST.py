import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def pint(): return int(input())


def pmap(): return map(int, input().strip().split())


def plist(): return list(map(int, input().strip().split()))


def pstr(): return input().strip()

def check(a,b,c):
    if a + b >= c and b + c >= a and c + a >= b: return True
    else: return False

t = int(input())

while t:
    t -= 1
    a,b,c = plist()
    if check(a,b,c):
        print(0)
    else:
        d = sorted([a,b,c])
        print(d[2]-d[1]-d[0])
