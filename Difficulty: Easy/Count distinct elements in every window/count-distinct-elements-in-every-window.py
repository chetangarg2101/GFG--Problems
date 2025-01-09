
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        hashMap = defaultdict(int)
        ans = []
        
        for i in range(k):
            hashMap[arr[i]] = hashMap.get(arr[i], 0) + 1
        
        ans.append(len(hashMap))
        
        for i in range(1, n):
            if i + k - 1 < n:
                if hashMap[arr[i - 1]] == 1:
                    del hashMap[arr[i - 1]]
                else:
                    hashMap[arr[i - 1]] -= 1
                hashMap[arr[i + k - 1]] = hashMap.get(arr[i + k - 1], 0) + 1
                ans.append(len(hashMap))
        return ans


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends