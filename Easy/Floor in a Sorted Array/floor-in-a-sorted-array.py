class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low, high = 0, N - 1
        result = -1  # Initialize result to -1

        while low <= high:
            mid = (low + high) // 2

            if A[mid] > X:    #If arr[mid] is greater than x
                high = mid - 1
            else:
                result = mid      #returning the index value
                low = mid + 1  #If arr[mid] is lesser than x

        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends