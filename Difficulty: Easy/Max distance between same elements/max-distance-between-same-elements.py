class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        hash={}
        c=0
        for i in range(len(arr)):
            if arr[i] not in hash:
                hash[arr[i]]=i
            else:
                c=max(c,i-hash[arr[i]])
        return c



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends