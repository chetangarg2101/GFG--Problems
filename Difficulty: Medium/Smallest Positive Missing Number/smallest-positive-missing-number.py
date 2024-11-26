#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        # Identify the largest value in the array
        max_val = max(arr)
        
        # If all numbers are negative or zero, return 1
        if max_val < 1:
            return 1
        
        # Create a list to track which positive numbers exist
        presence_tracker = [False] * max_val
        
        # Mark existing positive numbers in the tracker
        for num in arr:
            if 0 < num <= max_val:
                presence_tracker[num - 1] = True
        
        # Find the first missing positive number
        for i in range(max_val):
            if not presence_tracker[i]:
                return i + 1
        
        # If all numbers up to the maximum are present, return the next positive number
        return max_val + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends