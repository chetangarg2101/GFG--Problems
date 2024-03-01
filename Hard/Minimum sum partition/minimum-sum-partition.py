#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
		total_sum = sum(arr)
        max_possible_sum = total_sum // 2 + 1
        
        # Create a DP array to store the possible subset sums
        dp = [[False] * (max_possible_sum) for _ in range(n + 1)]
        
        # Initialize the first column as True, because we can make 0 sum with empty subset
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the DP array
        for i in range(1, n + 1):
            for j in range(1, max_possible_sum):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Find the minimum difference
        min_diff = float('inf')
        for j in range(max_possible_sum):
            if dp[n][j]:
                min_diff = min(min_diff, total_sum - 2 * j)
        
        return min_diff
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends