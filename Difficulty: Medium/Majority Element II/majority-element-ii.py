class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        l=[]
        count=0
        arr.sort()
        for i in range(len(arr)):
            curr=arr[i]
            if curr==arr[i-1]:
                count+=1
            else:
                count=0
            if count>=len(arr)//3:
                l.append(arr[i])
        return sorted(list(set(l)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends