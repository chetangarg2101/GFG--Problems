#User function Template for python3

class Solution:
    def findWinner(self, n, A):
        # code here
        xor_sum = 0
        for num in A:
            xor_sum^= num
        if xor_sum ==0 or n % 2 == 0:
           return 1
        else:
           return 2    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends