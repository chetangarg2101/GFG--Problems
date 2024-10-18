#User function Template for python3

class Solution:
    def roundToNearest (self, nstr) : 
        #Complete the function
        a=list(nstr)
        l=len(a)
        if l==1:
            return '0'
        if int(a[l-1])>5:
            i = l - 2
            while i >= 0 and a[i] == '9':
                a[i] = '0'
                i -= 1
            if i >= 0:
                a[i] = str(int(a[i]) + 1)
            else:
                a.insert(0, '1')
        a[l-1]='0'
        return ''.join(a)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends