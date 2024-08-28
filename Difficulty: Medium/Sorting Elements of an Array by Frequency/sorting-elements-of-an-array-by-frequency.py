#User function Template for python3
 
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        d = {}
        

#Calculating the frequency of each element
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                

#Sorting the dictionary based on the frequency (descending) and then by element value (ascending)
        sorted_d = sorted(d.items(), key = lambda x: (-x[1], x[0]))
        

# Build the result list based on the sorted items
        result = []
        
        for key, value in sorted_d:
            result.extend([key]*value)
            
        return result



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

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends