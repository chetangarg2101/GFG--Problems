class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        n,m=len(mat),len(mat[0])
        ans=[[0]*(m) for _ in  range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][(m-k%m+j)%m]=mat[i][j]
        return ans
#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends