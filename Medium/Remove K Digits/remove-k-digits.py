#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        s = []
        for d in S:
            while K > 0 and s and s[-1] > d:
                s.pop()
                K -= 1
            s.append(d)
        while K > 0:
            s.pop()
            K -= 1
        result = ''.join(s).lstrip('0')
        return result if result else '0'
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends