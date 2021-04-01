import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


while True:
    in_ = int(input())
    if in_ == 42:
        break
    print(in_)