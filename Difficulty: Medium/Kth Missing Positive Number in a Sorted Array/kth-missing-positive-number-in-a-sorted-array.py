#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        def ok(mi):
            return arr[mi] - (mi+1) >= k
            
        lo, hi = 0, len(arr)
        while lo < hi:
            mi = lo+(hi-lo)//2
            if ok(mi):
                hi = mi
            else:
                lo = mi+1
        if lo == 0: 
            return k
        
        missing = arr[lo-1] - lo
        k -= missing
        return arr[lo-1]+k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends