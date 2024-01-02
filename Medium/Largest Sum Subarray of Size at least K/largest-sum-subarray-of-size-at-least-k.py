#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        ans=-float('inf')
        mn=[float('inf')]*(n+k)
        mn[k-1]=0
        pfs=a[0]
        for i,v in enumerate(a):
            if i>=1:
                pfs+=v
            i+=k
            mn[i]=min(mn[i-1],pfs)
            ans=max(ans,pfs-mn[i-k])
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends