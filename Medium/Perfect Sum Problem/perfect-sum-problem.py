#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		dp = [0]*(sum + 1)
		dp[0] = 1
		
		for i in arr:
		    
		    temp = dp[:]
		    for j in range(i, sum + 1):
		        dp[j] += temp[j - i]

		return dp[sum]%(10**9+7)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends