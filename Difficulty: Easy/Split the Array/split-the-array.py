#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		n = len(arr)
        total = 0
        for i in range(n):
            total ^= arr[i]
        if total != 0:
            return 0
        else:
            return int(pow(2, n-1)-1) % 1000000007



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends