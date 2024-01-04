#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        dic = {}
        for i in range(N):
            dic[arr[i]] = dic.get(arr[i], 0) + 1
        
        single_occurrence_element = -1
        for i in dic:
            if dic[i] == 1:
                single_occurrence_element = i
                break
        
        return single_occurrence_element  
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends