#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        curr=head
        n=0
        while curr:
            n=curr.data+n*10
            curr=curr.next
        n=n+1
        newhead=Node(n%10)
        n=n//10
        temp=newhead
        while n:
            newhead.next=Node(n%10)
            newhead=newhead.next
            n=n//10
        newhead=self.reverse(temp)
        return newhead
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends