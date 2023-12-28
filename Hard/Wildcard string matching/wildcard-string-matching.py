#User function Template for python3
import re
class Solution:
    def match(self, wild, pattern):
        # code here
        wild_regex = re.escape(wild).replace(r'\*', '.*').replace(r'\?', '.')
        match = re.fullmatch(wild_regex, pattern)
        
        return match is not None
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends