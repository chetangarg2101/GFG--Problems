#User function Template for python3

class Solution:
   def __init__(self):
     self.mod = 10**9+7
    
   def TotalWays(self, N):
		# Code here
	 a,b=2,3
     for i in range(3,N+1):
       b,a=(a+b)%self.mod,b
     return b**2%self.mod if N!=1 else a**2
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends