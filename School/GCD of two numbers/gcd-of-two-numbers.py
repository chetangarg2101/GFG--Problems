
class Solution:
    def gcd(self, A, B):
        # code here
        while B:
            A, B = B, A%B
        return A
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends