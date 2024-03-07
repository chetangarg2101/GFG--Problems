#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        l1 = set()
        if len(S) == 1:
            return [S]
        ch  = self.find_permutation(S[1:])

        for perm in ch:
            for i in range(len(perm)+1):
                l1.add(perm[:i] + S[0] + perm[i:])
        return list(l1)
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends