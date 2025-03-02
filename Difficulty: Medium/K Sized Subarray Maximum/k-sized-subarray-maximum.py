class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n = len(arr)
        q = []
        answer = []
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i),
        for i in range(k, n):
            answer.append(arr[q[0]])
            while q and q[0] <= i-k:
                q.pop(0) #pop(0) is O(N)
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        answer.append(arr[q[0]])
        return answer


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends