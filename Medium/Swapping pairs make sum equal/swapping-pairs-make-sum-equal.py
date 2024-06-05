class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum1,sum2 = 0,0
        
        for i in range(n):
            sum1 += a[i]
        for j in range(m):
            sum2 += b[j]
        
        a.sort()
        b.sort()
        left,right = 0,0
        
        while left <n and right <m:
            val = sum1 -(a[left])+(b[right])
            val1 = sum2+(a[left])-(b[right])
            
            if val == val1:
                return 1
            if val > val1:
                left += 1
            else:
                right += 1
        return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends