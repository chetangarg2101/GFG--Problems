#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        mini=len(arr[0])
        c=0
        ans=""
        for i in range(len(arr)):
            if(mini>len(arr[i])):
                mini=len(arr[i])
                c=i
                
        flag=0
        for i in range(len(arr[c])):
            for j in range(len(arr)):
                if arr[j][i]!=arr[c][i]:
                    flag=1
                    
                    break
            if flag==1:
                break
            
            if(flag!=1):
                ans+=arr[c][i]
            flag=0
                    
        if ans=="":
            return "-1"
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends