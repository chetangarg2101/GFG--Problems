#User function Template for python3

def isValid(s):
    #code here
    a=s.split('.')
    for i in a:
        try:
            if int(i)>255:
                return False
            if len(str(int(i)))!=len(i):
                return False
        except:
            return False
    return len(a)==4
#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends