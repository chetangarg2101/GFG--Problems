#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        n=len(mat)
        prev_row_head=None
        curr_row_head=None
        prev=None
        head=None
        for i in range(n):
            for j in range(n):
                if j==0:
                    if i==0:
                        head=Node(mat[i][j])
                        prev=head
                    else:
                        prev=Node(mat[i][j])
                    curr_row_head=prev
                else:
                    prev.right=Node(mat[i][j])
                    prev=prev.right
                if i!=0:
                    prev_row_head.down=prev
                    prev_row_head=prev_row_head.right
                if j==n-1:
                    prev_row_head=curr_row_head
        return head


#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends