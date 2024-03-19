#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        if not arr or n == 0:
            return "-1"

        arr.sort()
        common_prefix = ""
    
        for i in range(min(len(arr[0]), len(arr[n - 1]))):
            if arr[0][i] == arr[n - 1][i]:
                common_prefix += arr[0][i]
            else:
                break
    
        return common_prefix if common_prefix else "-1"
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends