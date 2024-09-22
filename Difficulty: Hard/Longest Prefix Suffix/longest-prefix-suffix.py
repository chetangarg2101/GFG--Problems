#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
		n = len(str)
        p = [0]*(n)
        
        for i in range(1,n):
            j = p[i-1]
            while j>0 and str[j]!=str[i]:
                j = p[j-1]
            p[i] = j + int(str[j] == str[i])
        return p[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends