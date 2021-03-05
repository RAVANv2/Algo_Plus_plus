
import sys
sys.setrecursionlimit(10**6)


heap = []
heap.append([1,3])
heap.append([4,6])
heap.append([2,7])

import heapq

heapq.heapify(heap)

print(heap)
heapq.heappop(heap)
print(heapq.heappop(heap))

heapq.hea

from collections import defaultdict