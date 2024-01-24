#User function Template for python3

class Solution:
    def isTree(self, n, m, edges):
        # Code here
        adj_list = {i: [] for i in range(n)}

        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            return True
        if not dfs(0, -1) or len(visited) != n:
            return 0
        return 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
# } Driver Code Ends