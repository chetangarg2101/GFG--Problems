#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        ht1 = [0]*26
        ht2 = [0]*26
        l1 = len(str1)
        l2 = len(str2)
        if(l1!=l2):
            return False
        for i in range(l2):
            is2 =  ord(str2[i])-ord('a')
            is1 =  ord(str1[i])-ord('a')
            if ht2[is2]==0:
                if(ht1[is1]!=0):
                    return False
                else:
                    ht1[is1] = 1
                    ht2[is2] = str1[i]
            else:
                if(str1[i]!=ht2[is2]):
                    return False
        return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends