import functools

def fitness(item):
    return item[0]
def compare(item1, item2):
    return fitness(item1) - fitness(item2)



t = int(input())

while t:
    t -= 1

    N = int(input())
    a = list(map(int,input().strip().split()))

    index_a = []


    for i in range(len(a)):
        index_a.append([a[i],i])

    index_a = sorted(index_a, reverse=True,key=functools.cmp_to_key(compare))

    hour = 0

    final = [-1 for _ in range(len(index_a))]
    for i in range(len(index_a)):
        hour += 1
        final[index_a[i][1]] = hour

    for ele in final:
        print(ele, end=' ')