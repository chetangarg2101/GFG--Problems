#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        last = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in last and last[s[right]] >= left:
                left = last[s[right]] + 1
            last[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends