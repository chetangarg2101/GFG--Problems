#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		num = int(s, 2)
        return bin(num+1)[2:] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends