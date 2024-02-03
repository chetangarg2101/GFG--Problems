#User function Template for python3

class Solution:
    def longestPalin(self, S):
        # code here
        ans = S[0]
        for i in range(len(S)):
            j = i+len(ans)+1
            while j<len(S)+1:
                p = S[i:j]
                if p == p[::-1]:
                    ans = p
                j += 1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends