#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        start=1 if s.startswith("-") else 0
        ans = 0
        for i in range(start,len(s)):
           if ord(s[i])<=ord("9") and ord(s[i])>=ord("0"):
              ans=ans*10+ord(s[i])-ord("0")
           else:
              return -1
        return -1*ans if start else ans
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends