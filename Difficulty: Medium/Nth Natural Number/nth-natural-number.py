#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        t = 1
        res = 0
        base = 9
        while(n>0):
            res = res+(n%base)*t
            n = n//base
            t = t*10
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends