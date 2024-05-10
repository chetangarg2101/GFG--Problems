#User function Template for python3

class Solution:
    def gcd(self , A , B):
        if A == 0:
            return B
        else:
            return self.gcd(B % A , A)
            
    def lcmAndGcd(self, A , B):
        
        
        lcm = (A*B)//self.gcd(A , B)
        return [lcm , self.gcd(A ,  B )]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends