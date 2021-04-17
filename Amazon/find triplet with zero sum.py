class Solution:
    #Function to find triplets with zero sum.
    def findTriplets(self, arr, n):
        arr = sorted(arr)
        for i in range(n-1):
            j = i + 1
            k = n - 1
            var = 0
            while j < k:
                var = arr[i] + arr[j] + arr[k]
                if var > 0:
                    k -= 1
                elif var < 0 :
                    j += 1
                elif var == 0:
                    return 1
        return 0