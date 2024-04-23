#User function Template for python3
import numpy as np
class Solution:
    def firstElement (self, n):
        # code here 
        a,b=1,0
        while n:
            b,a=a,(a+b)%1000000007
            n-=1
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends