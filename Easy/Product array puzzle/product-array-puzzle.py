#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        if n==1:
            return [1]
        result=[1]*n
        l,r=1,1
        for i in range(n):
            result[i]*=l
            l*=nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=r
            r*=nums[i]
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends