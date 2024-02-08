#User function Template for python3
from bisect import bisect_left
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        lis = []
        lis.append(a[0])
        for i in a:
            if i > lis[-1]:
                lis.append(i)
            else:
                idx = bisect_left(lis, i)
                if idx < len(lis):
                    lis[idx] = i
        return len(lis)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends