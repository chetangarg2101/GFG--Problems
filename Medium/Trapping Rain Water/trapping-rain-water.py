
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        left=[arr[0]]
        mx=left[-1]
        for i in arr[1:]:
            mx=max(i,left[-1])
            left.append(mx)
        right=[arr[-1]]
        mx=right[-1]
        for i in arr[:-1][::-1]:
            mx=max(i,right[-1])
            right.append(mx)
        right=right[::-1]
        ans=0
        for idx,height in enumerate(arr):
            ans+=min(left[idx],right[idx])-height
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends