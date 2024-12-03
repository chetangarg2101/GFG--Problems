#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        dp = [0]*len(s1)
        
        for i in range(1, len(s1)):
            j = dp[i-1]
            while j > 0 and s1[i] != s1[j]:
                j = dp[j-1]
                
            dp[i] = j + int(s1[i] == s1[j])
            
        i, j = 0, 0
        while i < len(s2):
            if s2[i] == s1[j]:
                i += 1
                j += 1
                if i == len(s2) and s1[j:] + s1[:j] == s2:
                        return True
            else:
                if j > 0:
                    j = dp[j-1]
                else:
                    i += 1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends