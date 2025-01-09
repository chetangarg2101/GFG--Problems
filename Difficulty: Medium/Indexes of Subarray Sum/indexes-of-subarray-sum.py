#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code heren = len(arr)
        n = len(arr)
        start = 0
        current_sum = 0
    
        for end in range(n):
            current_sum += arr[end]
    
            # Shrink the window from the left if current_sum is greater than target
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
    
            # Check if we found a subarray with the desired sum
            if current_sum == target:
                return [start + 1, end + 1]  # 1-based indices
    
        return [-1]  # If no subarray is found




#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends