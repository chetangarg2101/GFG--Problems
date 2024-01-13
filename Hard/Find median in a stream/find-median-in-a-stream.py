#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3

''' 
use globals min_heap and max_heap, as per declared in driver code
use heapify modules , already imported by driver code
'''
from heapq import heappush,heappop
class Solution:
    def __init__(self):
        self.small = []
        self.large = []
        
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        if len(self.small) > len(self.large):
            ele = -1 * heappop(self.small)
            heappush(self.large, ele)
            
        if len(self.small) < len(self.large):
            ele = heappop(self.large)
            heappush(self.small, -1 * ele)
        
        
    '''    
    You don't need to call getMedian it will be called itself by driver code
    for more info see drivers code below.
    '''
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1*self.small[0] + self.large[0]) / 2.0
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        heappush(self.small, -1 * x)
        if self.small and self.large and (-1*self.small[0]) > self.large[0]:
            ele = -1 * heappop(self.small)
            heappush(self.large,ele)
        self.balanceHeaps()

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends