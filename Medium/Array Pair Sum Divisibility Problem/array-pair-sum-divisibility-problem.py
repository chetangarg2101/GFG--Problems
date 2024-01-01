#User function Template for python3

class Solution:
   def canPair(self, nums, k):
		# Code here
	 mods = [0 for _ in range(k)]
	 for item in nums: 
	    mods[item % k] += 1
     i, j = 1, k - 1
     while i < j:
      if mods[i] != mods[j]:
            
         return False
      i += 1
      j -= 1
     return mods[0] % 2 == 0 and (k % 2 == 1 or mods[k // 2] % 2 == 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends