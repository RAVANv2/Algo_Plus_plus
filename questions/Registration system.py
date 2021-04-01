import sys

from collections import defaultdict
import re
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

name = {}
name = defaultdict(lambda:"",name)

while t:
    t -= 1
    entry = input()

    if name[entry] == "":
        print("OK")
        name[entry] = entry + "0"
    else:
        name[entry] = entry + str(int(''.join(re.findall(r'\d+',name[entry])))+1)
        print(name[entry])
