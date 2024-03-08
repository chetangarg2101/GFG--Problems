
class Solution:
    def minDist(self, arr, n, x, y):
        ele1=[]
        ele2=[]
        res=[]
        if x in arr and y in arr:
            for i in range(n):
                if arr[i]==x:
                    ele1.append(i)
            for j in range(n):
                if arr[j]==y:
                    ele2.append(j)
            for i in ele1:
                for j in ele2:
                    res.append(abs(i-j))
            return min(res)
        else:
            return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends