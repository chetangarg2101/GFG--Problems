#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
		dp = [[0, 0] for _ in range(n+1)]
        dp[0] = [1, 0]
        
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]
            if i > 1:
                dp[i][1] = sum(dp[i-2])
        return sum(dp[-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends