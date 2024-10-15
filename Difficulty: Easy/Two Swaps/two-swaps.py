class Solution:
    def checkSorted(self, arr):
        #code here
        cnt = 0
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                cnt += 1
        if cnt == 3 or cnt == 0:
            return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends