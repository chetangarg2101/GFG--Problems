#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        num = n
        sum = 0
        
        while num > 0:
            dig = num % 10     
            cube = pow(dig, 3)  
            sum += cube         
            num = num // 10     
        
        if sum == n:
            return "true"
        else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends