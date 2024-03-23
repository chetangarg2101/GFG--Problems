#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        ans = [0, 1]
        for i in range(2, n+1):
            ans.append((ans[i-1] + ans[i-2]) % (10**9 + 7)) 
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends