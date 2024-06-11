
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        ans = 0

        

        for i in range(4, n + 1):

            contains_four = False

            a = i

            while a > 0:

                if a % 10 == 4:

                    contains_four = True

                    break

                a //= 10

            if contains_four:

                ans += 1

        

        return ans
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends