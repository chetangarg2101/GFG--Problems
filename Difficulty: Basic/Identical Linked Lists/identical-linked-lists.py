# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def areIdentical(head1, head2):
    # Code here
    while head1 is not None and head2 is not None:
        # Compare data of both nodes
        if head1.data != head2.data:
            return False
        
        # Move to the next node in both lists
        head1 = head1.next
        head2 = head2.next
    
    return head1 is None and head2 is None

def append(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def print_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

head1 = None
for i in [1, 2, 3, 4, 5, 6]:
    head1 = append(head1, i)


head2 = None
for i in [99, 59, 42, 20]:
    head2 = append(head2, i)


head3 = None
head4 = None
for i in [1, 2, 3, 4, 5]:
    head3 = append(head3, i)
    head4 = append(head4, i)


#{ 
 # Driver Code Starts
# Node Class
class node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if (areIdentical(head1, head2)):
            print('true')
        else:
            print('false')

# } Driver Code Ends