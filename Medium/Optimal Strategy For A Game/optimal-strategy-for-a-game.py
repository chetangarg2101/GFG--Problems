#User function Template for python3
#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        mem = {}
        def dfs(l,r):
            if (l,r) in mem :
                return mem[(l,r)]
            if l > r :
                return 0 
            poss1 = arr[l] + min(dfs(l+1, r-1), dfs(l+2,r))
            poss2 = arr[r] + min(dfs(l, r-2), dfs(l+1, r-1))
            
            maxi = max(poss1, poss2)
            mem[(l,r)] = maxi
            return mem[(l,r)]
        return dfs(0,n-1)
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
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends