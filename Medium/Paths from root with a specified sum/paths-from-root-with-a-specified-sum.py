#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def printPaths(self, root, target_sum):
        #code here
        ans = 0
        nodes_list = []
    
        def dfs(node, path):
            nonlocal ans
            nonlocal nodes_list
        
            ans += node.data
            path.append(node.data)
        
            if ans == target_sum:
                nodes_list.append(path[:])
        
            if node.left:
                dfs(node.left, path)
        
            if node.right:
                dfs(node.right, path)
        
            ans -= node.data
            path.pop()
    
        dfs(root, [])
        return nodes_list
#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        sum=int(input())
        s=input()
        root = buildTree(s)
        ob = Solution()
        ans = ob.printPaths(root, sum)
        ans = sorted(ans)
        
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                print(ans[i][j], end=" ")
                
            print()
            
# } Driver Code Ends