#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        start = 0
        end = n
        ans = -1
        while start <= end:
            mid = start + (end-start)//2
            if mid*mid == n:
                return mid
            if mid*mid > n:
                end = mid -1
            else:
                ans = mid
                start = mid+1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends