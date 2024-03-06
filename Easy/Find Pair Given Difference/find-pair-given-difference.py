#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        i,j=0,1
        n=N
 

        while j < len(arr):
            if arr[j] - arr[i] == n:
                return True
            elif arr[j] - arr[i] < n:
                j += 1
            elif arr[j] - arr[i] > n:
                i += 1
                if i==j:
                    j+=1
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends