
def find_ways(n):
    # Base condition
    if n < 0:
        return 0

    if n in [0,1]:
        return 1 

    # Recursive condition
    return find_ways(n-1) + find_ways(n-2) + find_ways(n-3)

def find_with_dp(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

if __name__ == "__main__":

    step = int(input())
    print(find_ways(step))
    print(find_with_dp(step))