# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        nums=arr
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        n = len(nums)
        dp = [False] * (target_sum + 1)
        dp[0] = True 
        for num in nums:
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target_sum]
#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends