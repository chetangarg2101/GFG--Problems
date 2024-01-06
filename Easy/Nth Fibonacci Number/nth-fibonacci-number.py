
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        m=(10**9)+7
        value = 0
        x_min_two = 0
        x_min_one = 1
        for i in range(n-1):
            # important to include %m here and not at the end of function
            value = (x_min_one + x_min_two) % m 
            x_min_two = x_min_one
            x_min_one = value
            
        return value
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends