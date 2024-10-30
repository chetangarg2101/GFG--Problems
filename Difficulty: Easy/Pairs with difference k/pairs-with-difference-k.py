#User function Template for python3
from collections import Counter
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	c=0
        seen=Counter(arr)
        for num in seen:
           if k>0:
               if num+k in seen:
                   c+=seen[num]*seen[num+k]
           else:
               c+=(seen[num]*(seen[num]-1))//2
        return c




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends