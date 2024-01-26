#User function Template for python3
class Solution:


	def generateNextPalindrome(self,num, n ) :
	    # code here
	    def inc(left):         #8874899999
            last = len(left) - 1
            while(left[last] == 9):
               left[last] = 0
               last -= 1
            left[last] += 1
            
            return left
        
        if(n == 1 and num[0] < 9):     #(num = [5] , n =1)
            num[0] += 1
            return num
        
            
        odd = n%2
        
        if(odd):
            center = [num[n//2]]
        else:
            center = []
            
        left = num[:n//2]
        right = left[::-1]
        
        palindrome = left + center + right
        if(str(palindrome) > str(num)):
            return palindrome
            
        else:
            if(left.count(9) == len(left)):         #999999
                num = [int(x) for x in ('1' + (n-1)*'0' + '1')]
                return num
                
            elif(center):
                if(center[0] < 9):
                    center[0] += 1
                    num = left + center + right 
                    return num
                    
                else:
                    center[0] = 0
            
            left = inc(left)
            right = left[::-1]
                
            num = left + center + right        
                
            return num
#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends