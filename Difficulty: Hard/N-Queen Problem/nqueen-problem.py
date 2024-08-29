#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        row = [0] * n
        upper_diagonal = [0] * (2*n - 1)
        lower_diagonal = [0] * (2*n -1)
        ans = []
        
        
        def recur(col,res):
            if col == n:
                ans.append(res[:])
                return
            
            for r in range(n):
                if (
                    row[r] == 0 and
                    upper_diagonal[r + col] == 0 and
                    lower_diagonal[n - 1 + col - r] == 0
                    ):
                    row[r] = 1
                    upper_diagonal[r + col] = 1
                    lower_diagonal[n - 1 + col - r] = 1
                    res.append(r + 1)
                    recur(col + 1,res)
                    row[r] = 0
                    upper_diagonal[r + col] = 0
                    lower_diagonal[n - 1 + col - r] = 0
                    res.pop()
        
        recur(0,[])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends