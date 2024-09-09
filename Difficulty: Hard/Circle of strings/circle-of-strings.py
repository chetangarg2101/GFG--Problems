#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def isCircle(self, arr):
        # code here
        graph = defaultdict(list)
        in_degree = [0] * 26
        out_degree = [0] * 26
        
        def char_to_index(c):
            return ord(c) - ord('a')
        
        # Build the graph and degree counts
        for word in arr:
            start = char_to_index(word[0])
            end = char_to_index(word[-1])
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Check if the in-degree and out-degree are the same for each vertex
        for i in range(26):
            if in_degree[i] != out_degree[i]:
                return 0
        
        # Function to perform DFS to check connectivity
        def dfs(v, visited):
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    dfs(u, visited)
        
        # Find the first character that has an edge (non-zero degree)
        start_node = -1
        for i in range(26):
            if out_degree[i] > 0:
                start_node = i
                break
        
        # If there's no such node, return 0
        if start_node == -1:
            return 0
        
        # Check if all vertices with non-zero degrees are reachable from start_node
        visited = [False] * 26
        dfs(start_node, visited)
        
        # Check if all non-zero degree vertices are visited
        for i in range(26):
            if out_degree[i] > 0 and not visited[i]:
                return 0
        
        # Now check the reverse graph for strong connectivity
        reverse_graph = defaultdict(list)
        for i in range(26):
            for j in graph[i]:
                reverse_graph[j].append(i)
        
        visited = [False] * 26
        dfs(start_node, visited)  # DFS on the reversed graph
        
        for i in range(26):
            if out_degree[i] > 0 and not visited[i]:
                return 0
        
        # If all conditions are satisfied, return 1
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends