#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        
        # code here
        ans=sm1=sm0=0
        for ix,ve in enumerate(s):
            sm1=(sm0*10+int(ve)*(ix+1))%(10**9+7)
            ans=(ans+sm0)%(10**9+7)
            sm0=sm1
        return (ans+sm0)%(10**9+7)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends