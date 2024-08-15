#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [0 for _ in range(n + 1)]
        for coin in [x, y, z]:
            for i in range(coin, n + 1):
                if i == coin or dp[i - coin] > 0:
                    dp[i] = max(dp[i], dp[i - coin] + 1)
        
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends