#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        #Your code here
        diff = [0] * (maxx + 2)
        for i in range(n):
            diff[l[i]] += 1
            diff[r[i] + 1] -= 1
        max_freq = 0
        result = 0
        curr_freq = 0
        for i in range(maxx + 1):
            curr_freq += diff[i]
            if curr_freq > max_freq:
                max_freq = curr_freq
                result = i
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends