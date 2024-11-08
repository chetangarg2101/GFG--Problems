#User function Template for python3

class Solution:
    def minSum(self, arr):
        # code here
        def add(xs, ys):
            m, n = len(xs), len(ys)
            i, j, carry = m-1, n-1, 0
            ans = []
            while i >= 0 or j >= 0 or carry > 0:
                v = carry
                if i >= 0:
                    v += xs[i]
                    i -= 1
                if j >= 0:
                    v += ys[j]
                    j -= 1
                carry = v//10
                ans.append(v%10)
            while ans and ans[-1] == 0:
                ans.pop()
            return ans[::-1]
                
        arr.sort()
        xs, ys = [], []
        i, n = 0, len(arr)
        while i < n:
            xs.append(arr[i])
            i += 1
            if i < n:
                ys.append(arr[i])
                i += 1
        
        return "".join(str(e) for e in add(xs, ys))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends