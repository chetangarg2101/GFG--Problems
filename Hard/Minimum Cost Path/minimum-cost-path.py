import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		#Code here
		heap=[(grid[0][0],0,0)]
        heapq.heapify(heap)
        s=set()
        s.add((0,0))
        n=len(grid)
        while heap:
            dis, i, j=heapq.heappop(heap)
            
            if i==n-1 and j==n-1:
                return dis
            di=[(-1,0),(1,0),(0,-1),(0,1)]
            
            for k in di:
                r=i+k[0]
                c=j+k[1]
                if r>=0 and r<n and c>=0 and c<n and (r,c) not in s:
                    heapq.heappush(heap,(dis+grid[r][c],r,c))
                    s.add((r,c))
        return dis
#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends