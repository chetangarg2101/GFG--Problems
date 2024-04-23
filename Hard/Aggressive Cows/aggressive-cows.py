#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        def possibleDistCows(m, k, n):
            cnt = 1
            prev = stalls[0] # cow always allocate in greedy fashion
            for i in range(1, n):
                if(stalls[i] - prev < m):
                    continue
                else:
                    cnt += 1
                    prev = stalls[i]
            return cnt >= k
        stalls.sort()
        low = 1
        high = stalls[n-1] - stalls[0]
        # apply binary search
        while(low <= high):
            m = (low + high)//2
            r = possibleDistCows(m, k, n)
            if(not(r)):
                high = m - 1
            else:
                r1 = possibleDistCows(m+1, k, n)
                if (not(r1)):
                    return m
                else:
                    low = m + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends