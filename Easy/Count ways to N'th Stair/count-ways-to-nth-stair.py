#User function Template for python3


class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):

        mod = 1000000007
        # code here
        if n <= 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            if i%2 == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
        return dp[n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        ob = Solution()
        print(ob.countWays(n))

# } Driver Code Ends