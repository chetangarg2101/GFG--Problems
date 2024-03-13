# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        hei=len(mat)
        wid=hei
        ans=[]
        updwn=1
        for x in range(2*wid-1):
            if updwn==1:
                ycur=hei-1
                xcur=x-hei+1
            else:
                ycur=0
                xcur=x
            for y in range(hei):
                if 0<=xcur<wid:
                    ans.append(mat[ycur][xcur])
                xcur+=updwn
                ycur-=updwn
            if updwn==1:
                updwn=-1
            else:
                updwn=1
        return ans
#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends