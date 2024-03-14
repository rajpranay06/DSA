'''

You are given a set of N jobs where each job comes with a deadline and profit. The profit can only be earned upon completing the job within its deadline. 
Find the number of jobs done and the maximum profit that can be obtained. Each job takes a single unit of time and only one job can be performed at a time.

Examples

Example 1:

Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output: 2 60
Explanation: The 3rd job with a deadline 1 is performed during the first unit of time .The 1st job is performed during the second unit of time as its deadline is 4.
Profit = 40 + 20 = 60

Example 2:

Input: N = 5, Jobs = {(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)}
Output: 2 127
Explanation: The  first and third job both having a deadline 2 give the highest profit. 
Profit = 100 + 27 = 127

Approach:  
The strategy to maximize profit should be to pick up jobs that offer higher profits. Hence we should sort the jobs in descending order of profit. 
Now say if a job has a deadline of 4 we can perform it anytime between day 1-4, but it is preferable to perform the job on its last day. 
This leaves enough empty slots on the previous days to perform other jobs.

Basic Outline of the approach:-

Sort the jobs in descending order of profit. 
If the maximum deadline is x, make an array of size x .Each array index is set to -1 initially as no jobs have been performed yet.
For every job check if it can be performed on its last day.
If possible mark that index with the job id and add the profit to our answer. 
If not possible, loop through the previous indexes until an empty slot is found.

'''

from os import *
from sys import *
from collections import *
from math import *

def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit

    # Sort jobs in descending aorder acc to their profit  
    jobs.sort(key = lambda x:x[2], reverse = True)
    n = len(jobs)
    maxDeadline = jobs[0][1]

    # Get the maxDeadline of the jobs
    for i in range(1, n):
        maxDeadline = max(maxDeadline, jobs[i][1])
    
    totalJobs = 0
    maxProfit = 0
    jobsFilled = [-1]*(maxDeadline+1)

    for i in range(n):
        for j in range(jobs[i][1], 0, -1):
            # If the jobsFilled slot is not filled
            # Add it to maxProfit and fill the job 
            if jobsFilled[j] == -1:
                jobsFilled[j] = i
                totalJobs += 1
                maxProfit += jobs[i][2]
                break
    
    return [totalJobs, maxProfit]

'''

Time Complexity: O(N log N) + O(N*M).

O(N log N ) for sorting the jobs in decreasing order of profit. O(N*M) since we are iterating through all N jobs and for every job we are checking from the last deadline, say M deadlines in the worst case.

Space Complexity: O(M) for an array that keeps track on which day which job is performed if M is the maximum deadline available.

'''

'''

Approach 2: Using heaps

Push profits into heap, if len(heap) is greater than curr deadline pop the heap

'''

from os import *
from sys import *
from collections import *
from math import *
import heapq

def jobScheduling(jobs):

    jobs.sort(key=lambda x: (x[1], -x[2]))

    minHeap = []
    for _, deadline, profit in jobs:
        heapq.heappush(minHeap, profit)
        if len(minHeap) >= deadline+1:
            heapq.heappop(minHeap)
    
    return [len(minHeap), sum(minHeap)]
