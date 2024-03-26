#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        #code here
        ln = len(n)
        flag = 0
        for i in range(ln-1):
            a = n[0:i+1]
            for j in range(i+1,ln):
                p = int(a)
                b = n[i+1:j+1]
                x = a + b
                b = int(b)
                if len(x) == ln: continue
                while len(x)<ln:
                    c = p+b
                    h = str(c)
                    x += h
                    p = b
                    b = c
                if x ==  n:
                    flag = 1
        return 1 if flag == 1 else 0

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends