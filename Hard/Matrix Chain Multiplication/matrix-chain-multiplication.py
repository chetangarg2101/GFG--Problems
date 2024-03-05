#User function Template for python3

class Solution:
    def matrixMultiplication(self, N, arr):
        # Create a table to store the minimum number of multiplications
        # dp[i][j] will store the minimum number of multiplications needed
        # to multiply matrices from i to j
        dp = [[0] * N for _ in range(N)]

        # Fill the table diagonally
        # i represents the starting matrix
        # j represents the ending matrix
        for length in range(2, N):
            for i in range(1, N - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    # Calculate the number of multiplications needed to
                    # multiply matrices from i to j using matrix at k as pivot
                    cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        # The result is stored in dp[1][N - 1]
        return dp[1][N - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends