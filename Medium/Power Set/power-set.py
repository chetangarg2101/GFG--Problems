#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
        last = 1<<n
        arr = []
        for i in range(last):
            subs = ""
            for j in range(n):
                if 1<<j & i:
                    subs+=s[j]
            arr.append(subs)
            
        arr.sort()
        return arr[1:]
#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends