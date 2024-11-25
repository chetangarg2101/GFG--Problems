#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    s = sum(arr)
    running, minv = 0, float('inf')
    for e in arr:
        running += e
        minv = min(running, minv)
        running = min(0, running)
        
    running, maxv = 0, float('-inf')
    for e in arr:
        running += e
        maxv = max(running, maxv)
        running = max(0, running)
    return max(maxv, s - minv)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends