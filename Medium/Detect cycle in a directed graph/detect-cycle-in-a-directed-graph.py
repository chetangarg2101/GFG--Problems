#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = set() 
        def dfs(curr,recStack):
            visited.add(curr)
            recStack.add(curr)
            for nbr in adj[curr]:
                if nbr not in visited:
                    if dfs(nbr,recStack):
                        return True
                elif nbr in recStack:
                    return True
            recStack.remove(curr)
            return False
        
        
        for i in range(V):
            if i not in visited:
                recStack = set()
                if dfs(i,recStack):
                    return True
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends