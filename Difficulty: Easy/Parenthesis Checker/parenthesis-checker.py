
class Solution:
    def isBalanced(self, s):
        # code here
        st = []
        for c in s:
            if c in {'(','{','['}:
                st.append(c)
            elif c in { ')','}',']' }:
                if len(st) <= 0 : return False
                if c == ')' and st[-1]!='(':
                    return False
                if c == '}' and st[-1]!='{':
                    return False
                if c == ']' and st[-1]!='[':
                    return False
                st.pop()
        return len(st)==0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends