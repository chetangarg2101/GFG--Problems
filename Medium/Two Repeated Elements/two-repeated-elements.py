#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        seen = {}  # Dictionary to store count of elements
        result = []  # List to store the result

        # Iterate over the array
        for num in arr:
            # If number is already seen, append to result if it's the second time
            if num in seen:
                if seen[num] == 1:
                    result.append(num)
                seen[num] += 1
            else:
                seen[num] = 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends