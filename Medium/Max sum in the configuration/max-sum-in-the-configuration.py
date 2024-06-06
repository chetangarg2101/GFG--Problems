#User function Template for python3

def max_sum(a,n):
    #code here
    arr_sum = 0
    curr_val = 0

    for i in range(0, n):
        arr_sum = arr_sum + arr[i]
        curr_val = curr_val + (i*arr[i])

    max_val = curr_val

    for j in range(1, n):
        curr_val = curr_val + arr_sum - n * arr[n-j]
        if (curr_val > max_val):
            max_val = curr_val

    return max_val
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends