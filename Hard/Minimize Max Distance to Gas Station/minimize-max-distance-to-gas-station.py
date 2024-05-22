#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3

import math

class Solution:
    def findSmallestMaxDist(self, stations, K):
        def possible(distance):
            stations_to_add = 0
            for i in range(len(stations) - 1):
                gap = stations[i + 1] - stations[i]
                # Instead of floor, we use ceiling of gap / distance - 1
                stations_to_add += math.ceil(gap / distance) - 1
                if stations_to_add > K:
                    return False
            return stations_to_add <= K

        left = 0
        right = stations[-1] - stations[0]
        precision = 1e-5  # Slightly less precision to speed up convergence

        while right - left > precision:
            mid = (left + right) / 2.0
            if possible(mid):
                right = mid
            else:
                left = mid

        return right

#{ 
 # Driver Code Starts.
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        stations = list(map(int, input().split()))
        K = int(input())
        ob = Solution()
        print('%.2f' % ob.findSmallestMaxDist(stations, K))
# } Driver Code Ends