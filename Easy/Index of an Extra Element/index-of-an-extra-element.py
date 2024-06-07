class Solution:
    def findExtra(self,n,a,b):
        #add code here
        strt = 0
        end = n-2
        index = n-1
        while(strt <= end):
            mid = (end+strt)//2
            
            if (a[mid] == b[mid]):
                strt = mid+1
            else:
                index = mid
                end = mid-1
          
        return index
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends