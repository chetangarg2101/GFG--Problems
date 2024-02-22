# Your task is to complete this function
# Finction should return Integer
class Solution:
    def sequenceCount(self,s, t):
        # Code here
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j==len(t):
                return 1
            if i>=len(s) or j>=len(t):
                return 0
            if s[i]==t[j]:
                dp[(i, j)]= dfs(i+1, j+1)+dfs(i+1, j)
            else:
                dp[(i, j)]= dfs(i+1, j)
            return dp[(i, j)]%1000000007
        return dfs(0,0)%1000000007
#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends