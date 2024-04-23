#User function Template for python3

from collections import deque

class Solution:
    def findSequences(self, startWord, endWord, wordList):
        q = deque()
        res = set(wordList)
        if endWord not in res:
            return []
        ans = []
        q.append([startWord])
        while q:
            s = len(q)
            word_list = []
            for _ in range(s): 
                path = q.popleft()
                word = path[-1]
                if word == endWord:
                    ans.append(path)
                    continue
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        word1 = word[:i] + ch + word[i+1:]
                        if word1 in res:
                            path.append(word1)
                            q.append(path[:])
                            word_list.append(word1)
                            path.pop()
            for j in word_list:
                if j in res:
                    res.remove(j)
        return ans

#{ 
 # Driver Code Starts

from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends