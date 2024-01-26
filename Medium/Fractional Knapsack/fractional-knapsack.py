#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        for item in arr:
            item.ratio = item.value / item.weight
        arr.sort(key=lambda x: x.ratio, reverse=True)

        total_value = 0.0
        current_weight = 0

        for item in arr:
            if current_weight + item.weight <= W:
                total_value += item.value
                current_weight += item.weight
            else:
                remaining_weight = W - current_weight
                fraction = remaining_weight / item.weight
                total_value += fraction * item.value
                break  

        return total_value
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends