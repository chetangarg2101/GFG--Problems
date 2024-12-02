class Solution:
    def minChar(self, s):
        #Write your code here
        if len(s)==1:

            return 0

        k=""

        i=0

        j=len(s)-1

        ans=0

        while i<j:

            if s[i]==s[j]:

                i+=1

                j-=1

            else:

                ans=len(s)-j

                i=0

                while (s[i]==s[j]):

                    ans-=1

                    i+=1

                j-=1

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends