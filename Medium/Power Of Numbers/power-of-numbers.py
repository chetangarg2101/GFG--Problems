#User function Template for python3

class Solution:
    #Complete this function
    m = (10**9  + 7)
    def power(self,N,R):
        #Your code here
        if R == 0:
            return 1
        elif R&1 :
            return (N*((self.power(N,R//2))**(2)))%(self.m)
        else: 
            return ((self.power(N,R//2))**(2))%(self.m)
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends