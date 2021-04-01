

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        sum = a[0]
        sumBefore = a[0]
        for i in a[1:]:
            sum = max(i,sum+i)
            sumBefore = max(sumBefore,sum)
        return sumBefore
