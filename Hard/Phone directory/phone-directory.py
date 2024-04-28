#User function Template for python3
import re
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        hoi=sorted(contact)
        jo = ' '.join(hoi)
        lst = []
        x = ''
        for i in s:
            x += i
            d = []
            orderRegex= re.compile(r'(\b{})'.format(x))
            mo= orderRegex.findall('{}'.format(jo))
            if mo:
                for j in hoi:
                    if re.search(r'\b{}'.format(mo[0]),j):
                        d.append(j)
                    if len(d)>=2 and d[-1]==d[-2]:
                        d.remove(d[-1])
                lst.append(d)
            else:
                lst.append([0])

        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends