

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime

prime = SieveOfEratosthenes(10000000)

t = int(input())

while t:

    t -= 1

    L,R = list(map(int,input().strip().split()))

    for i in range(R+1,int(1e7)):
        if prime[i]:
            print(i)
            break