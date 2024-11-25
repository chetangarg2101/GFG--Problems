#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		if not arr:
            return 0
        
        # Initialize variables to track the current max and min product, and the global max
        cur_max = arr[0]
        cur_min = arr[0]
        global_max = arr[0]
        
        for num in arr[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max  # Swap when the current number is negative
            
            # Calculate the current max and min product including the current number
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            # Update the global max
            global_max = max(global_max, cur_max)
        
        return global_max


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends