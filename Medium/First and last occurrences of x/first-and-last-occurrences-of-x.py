#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        if x not in arr:
            return -1,-1
        first_occ = arr.index(x)
        last_occ = 0
        for i in range(len(arr)):
            if arr[i] == x :
               last_occ = i
        return first_occ,last_occ
#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends