class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        a, r, t, b = 0, len(mat[0])-1, 0, len(mat)-1
        result = []
        while a <= r and t <= b:
            for i in range(a, r+1):
                result.append(mat[t][i])
            t += 1
            for i in range(t, b+1):
                result.append(mat[i][r])
            r -= 1
            if t <= b:
                for i in range(r, a-1, -1):
                    result.append(mat[b][i])
                b -= 1
            if a <= r:
                for i in range(b, t-1, -1):
                    result.append(mat[i][a])
                a += 1
        return result


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends