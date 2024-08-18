#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        m = 0
        h = set()
        for i in arr:
            h.add(i)
        
        i = 0
        while k > 0:
            if i in h:
                k -= 1
            
            i += 1
        
        return i-1
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends