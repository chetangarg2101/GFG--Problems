#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		#code here
		max_diff = 0
        left_min = [0] * n
        right_max = [0] * n

        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(arr[i], left_min[i - 1])

        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(arr[i], right_max[i + 1])

        i = 0
        j = 0
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1

        return max_diff
#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends