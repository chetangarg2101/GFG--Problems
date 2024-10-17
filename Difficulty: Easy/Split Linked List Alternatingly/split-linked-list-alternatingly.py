#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        head1 = None
        head2 = None
        tail1 = None
        tail2 = None
        alter = True
        while head:
            new_node = Node(head.data)
            if alter:
                if head1 == None:
                    head1 = new_node
                    tail1 = head1
                else:
                    tail1.next = new_node
                    tail1 = new_node
            else:
                if head2 == None:
                    head2 = new_node
                    tail2 = head2
                else:
                    tail2.next = new_node
                    tail2 = new_node
                
            alter = not alter
            head = head.next
        return [head1, head2]
        


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        head = Node(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail.next = Node(arr[i])
            tail = tail.next

        ob = Solution()
        result = ob.alternatingSplitList(head)
        printList(result[0])
        printList(result[1])

# } Driver Code Ends