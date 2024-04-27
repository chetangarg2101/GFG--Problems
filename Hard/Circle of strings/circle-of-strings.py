#User function Template for python3
from collections import defaultdict
class Solution:
    def isCircle(self, N, A):
        # code here
        d,d1,v,c = defaultdict(list),defaultdict(int),set(),0
        
        for i in A:
            d[i[0]].append(i[-1])
            d1[i[0]]+=1
            d1[i[-1]]+=1
        
        def dfs(node):
            v.add(node)
            if node in d:
                for cnode in d[node]:
                    if cnode not in v:
                        dfs(cnode)
       
        for i in d:
            if i not in v:
                dfs(i)
                c+=1
        if c>1:
            return 0
            
        for i in d1:
            if d1[i]%2!=0:
                return 0
        return 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        A = input().split()
        
        ob = Solution()
        print(ob.isCircle(N, A))
# } Driver Code Ends