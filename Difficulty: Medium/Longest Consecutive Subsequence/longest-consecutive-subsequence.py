 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        unused = set(arr)
        max_len = 0
        for a in arr:
            if a not in unused:
                continue
            unused.remove(a)
            length = 1
            smaller = a - 1
            while smaller in unused:
                length += 1
                unused.remove(smaller)
                smaller -= 1
            bigger = a + 1
            while bigger in unused:
                length += 1
                unused.remove(bigger)
                bigger += 1
            max_len = max(max_len, length)
        return max_len


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
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends