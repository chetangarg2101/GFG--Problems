#User function Template for python3
'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        #Maximum Deadline
        max_deadline = max(job.deadline for job in Jobs)
        
        time_slot = [None]*(max_deadline + 1)
        total_job = 0
        total_profit = 0
        
        for job in Jobs:
            job_id  = job.id
            job_time = job.deadline
            profit = job.profit
            
            for i in range(job_time, 0, -1):
                if time_slot[i] is None:
                    time_slot[i] = job_id
                    total_job += 1
                    total_profit += profit
                    break
            
        return total_job, total_profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])

# } Driver Code Ends