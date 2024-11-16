#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	# Initialize the index for the next non-zero element
        non_zero_index = 0
        
        # Traverse through the array and move non-zero elements to the front
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1
        
        # Fill the remaining elements with zeros
        for i in range(non_zero_index, len(arr)):
            arr[i] = 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends