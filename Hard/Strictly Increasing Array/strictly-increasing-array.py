#User function Template for python3

class Solution:
	def min_operations(self,nums):
		# Code here
		from bisect import bisect_right
        n = len(nums)
        lis = [nums[0]]
        for i in range(1, n):
            num = nums[i] - i
            pos = bisect_right(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return n - len(lis)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends