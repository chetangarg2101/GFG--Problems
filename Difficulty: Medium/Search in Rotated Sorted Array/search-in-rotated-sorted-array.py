#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        low , high = 0 , len(arr)-1
        while low <= high:
            mi = (low + high) //2
            if arr[mi] == key:
                return mi
            if arr[mi] >= arr[low]:
                if arr[low] <= key and arr[mi]> key:
                    high = mi -1
                else:
                    low = mi + 1
            else:
                if arr[mi] < key and arr[high] >= key:
                    low = mi + 1
                else:
                    high = mi -1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends