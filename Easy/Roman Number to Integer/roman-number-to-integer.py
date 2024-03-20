#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for symbol in reversed(S):  
            value = roman_values[symbol]
            if value < prev_value: 
                result -= value
            else:
                result += value
            prev_value = value
        
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends