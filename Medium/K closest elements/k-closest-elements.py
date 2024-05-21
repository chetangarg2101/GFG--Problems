#User function Template for python3
from bisect import bisect_left as lower, bisect_right as upper
class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        sorted(arr)
        ans=[]
        u = upper(arr, x)
        l = lower(arr, x); 
        l-=1
        while(l>=0 and arr[l] == x): l-=1
        if l>=0 and arr[l]==x: l=-1
        ok=False; ok1=False; d=n+1; d1=n+1;
        while(len(ans)!=k):
            if l>=0: ok=True
            else: ok=False
            if u<n: ok1=True
            else: ok1=False
            if not ok and not ok1: break
            if ok : d=abs(x-arr[l])
            else: d=100000000000000000000000
            if ok1: d1=abs(x-arr[u])
            else: d1=100000000000000000000000
            i = min(d, d1)
            if i==d1: ans.append(arr[u]); u+=1;
            else: ans.append(arr[l]); l-=1;
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends