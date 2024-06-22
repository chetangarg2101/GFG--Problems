#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
		lst=[]
        stack=[]
        count1=0
        for i in S:
            if i=="(":
                count1+=1
                stack.append(count1)
                lst.append(count1)
            elif i==")":
                if len(stack)!=0:
                    lst.append(stack.pop(-1))
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends