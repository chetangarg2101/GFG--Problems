#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here
        bit=31
        ans=0
        while x:
            if x%2:
                ans+=1<<bit
            bit-=1
            x//=2
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends