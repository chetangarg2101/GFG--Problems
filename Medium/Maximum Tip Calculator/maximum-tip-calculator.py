
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        diff_list = [(arr[i], brr[i], abs(arr[i] - brr[i])) for i in range(n)]
        diff_list.sort(key=lambda x: x[2], reverse=True)
        
        total_tips = 0
        a_count = 0
        b_count = 0
        
        for tip_A, tip_B, _ in diff_list:
            if (tip_A >= tip_B and a_count < x) or b_count >= y:
                total_tips += tip_A
                a_count += 1
            else:
                total_tips += tip_B
                b_count += 1
        
        return total_tips
#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends