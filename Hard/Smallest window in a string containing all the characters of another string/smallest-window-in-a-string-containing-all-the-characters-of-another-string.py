#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        i=0
        j=0
        a=set()
        m_min=float('inf')
        d1={}
        while(j<len(p)):
            if p[j] not in d1:
                d1[p[j]]=1
            else:
                d1[p[j]]+=1
            j+=1
        j=0
        d2=d1
        while(i<len(s) and j<len(s)):    
            if s[j] in d1:
                d2[s[j]]-=1
                if d2[s[j]]<=0:
                    a.add(s[j])
                elif d2[s[j]]>0:
                    a.discard(s[j])
                
            while (len(a)==len(d1)):
                if s[i] in d1:
                    d2[s[i]]+=1
                    if d2[s[i]]>0:
                        a.remove(s[i])
                if j-i+1<m_min:
                    m_min=j-i+1
                    pi=i
                    qi=j
                i+=1
            j+=1
                
        if m_min==float('inf'):
            return -1
        return s[pi:qi+1:1]
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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends