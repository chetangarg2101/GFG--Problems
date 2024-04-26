#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    timer = 1
    def dfs(self,node,parent,vis,adj,tin,low,mark):
        vis[node] = 1
        tin[node]  = low[node] = self.timer
        self.timer += 1
        child = 0
        for i in adj[node]:
            if i == parent:
                continue
            if not vis[i]:
                self.dfs(i,node,vis,adj,tin,low,mark)
                low[node] = min(low[node],low[i])
                if(low[i]>=tin[node] and parent != -1):
                    mark[node] = 1
                child += 1
            else:
                low[node] = min(low[node],tin[i])
                
        if child>1 and parent == -1:
            mark[node] = 1
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        vis = [0] * V
        tin = [0] * V
        low = [0] * V
        mark = [0] * V
        for i in range(V):
            if not vis[i]:
                self.dfs(0,-1,vis,adj,tin,low,mark)
        ans = []        
        for i in range(V):
            if mark[i] == 1:
                ans.append(i)
        if len(ans) == 0:
            return [-1]
        return ans 

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends