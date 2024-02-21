#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        map,length = {0:-1},0 
        prefix_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum in map:
                length = max(length,i-map[prefix_sum])
            else:
                map[prefix_sum] = i 
        return length
#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends