#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        i = n-1
        while i > 0 and arr[i] <= arr[i-1]:
            i -= 1
        if i == 0:
            arr.reverse()
            return
        
        lo, hi = i, n
        while lo < hi:
            mi = lo+(hi-lo)//2
            if arr[mi] <= arr[i-1]:
                hi = mi
            else:
                lo = mi+1
        arr[i-1], arr[lo-1] = arr[lo-1], arr[i-1]
        arr[i:] = sorted(arr[i:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends