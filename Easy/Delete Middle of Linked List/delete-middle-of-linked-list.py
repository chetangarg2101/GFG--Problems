#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteMid(self,head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        
        #code here
        n=0
        temp1=head
        while temp1 !=None:
            n+=1
            temp1=temp1.next
        
        if n<=1:
            return None
        n//=2
        
        temp2=head
        while n>1:
            temp2=temp2.next
            n-=1
        temp2.next=temp2.next.next
        return head
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        obj = Solution();
        res=obj.deleteMid(ll.head)
        printList(res)
# } Driver Code Ends