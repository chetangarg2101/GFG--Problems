#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
		if n == 1:
            return 10  # All digits from 0 to 9 are valid single-length sequences
    
        # Define the valid moves for each digit
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 0, 5, 7, 9],
            9: [9, 6, 8]
        }
    
        # Initialize dp table
        dp = [[0] * 10 for _ in range(n + 1)]
    
        # Base case: sequences of length 1
        for digit in range(10):
            dp[1][digit] = 1
    
        # Fill the dp table for lengths from 2 to n
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = 0
                for neighbor in moves[digit]:
                    dp[length][digit] += dp[length - 1][neighbor]
    
        # Sum up the sequences of length n for all digits
        result = sum(dp[n][digit] for digit in range(10))
    
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends