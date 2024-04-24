#User function Template for python3
import math
class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        return max((sum((mat[y][x],mat[y-1][x-1],\
            mat[y+1][x+1],mat[y-1][x+1],mat[y-1][x],\
            mat[y+1][x] , mat[y+1][x-1]))\
            for y in range(1,n-1)\
            for x in range(1, m-1)),\
            default=-1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends