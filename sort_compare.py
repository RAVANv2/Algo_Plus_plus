
import sys
sys.setrecursionlimit(10**6)

import functools

lst = [[2,0],[5,2],[3,1],[3,3],[4,4]]

print(lst)

# if compare return +ve
#     item2 comes before item1
# if compare return -ve
#     item1 return before item2
# if compare return 0
#     return as per array order
def compare(item1, item2):
    return item2[0] - item1[0]

lst = sorted(lst, reverse=False,key=functools.cmp_to_key(compare))
print(lst)