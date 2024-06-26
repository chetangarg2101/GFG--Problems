#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here\nodes = set(list('abcdefghijklmnopqrstuvwxyz'[:K]))
        nodes = set(list('abcdefghijklmnopqrstuvwxyz'[:K]))
        graph = {node: set() for node in nodes}
        for i in range(N - 1):
            for a, b in zip(alien_dict[i], alien_dict[i + 1]):
                if a != b:
                    graph[a].add(b)
                    break

        visited = set()

        def dfs(node):
            if node in visited:
                return ''
            visited.add(node)
            s = ''
            for x in graph[node]:
                s += dfs(x)
            return s + node

        ans = ''
        for i in nodes:
            ans = dfs(i)[::-1] + ans
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends