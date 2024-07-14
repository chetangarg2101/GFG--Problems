#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        l = 0
        h = len(arr)-1
        
        while l < h :
            
            while l < h and arr[l] != 1:
                l += 1
            while l < h and arr[h] != 0:
                h -= 1
                
            arr[l], arr[h] = arr[h], arr[l]


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

# } Driver Code Ends