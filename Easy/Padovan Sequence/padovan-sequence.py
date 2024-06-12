#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        # code here
        mod = 10**9 + 7
        prev = curr = nxt = 1
        if n < 3:
            return 1
        for i in range(3, n+1):
            prev,curr,nxt   = curr, nxt, (prev+curr)%mod
        return nxt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends