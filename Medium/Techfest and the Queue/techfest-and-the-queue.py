
from typing import List


class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        smallest_prime_factor = [i for i in range(b + 1)]
        for i in range(2, int(b**0.5) + 1):
            if smallest_prime_factor[i] == i:
                for j in range(i*i, b + 1, i):
                    smallest_prime_factor[j] = i
        distinct_prime_factors_count = 0
        for num in range(a, b + 1):
            while num > 1:
                distinct_prime_factors_count += 1
                num //= smallest_prime_factor[num]
        return distinct_prime_factors_count

#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends