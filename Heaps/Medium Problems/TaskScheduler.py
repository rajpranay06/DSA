'''

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task.
Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. 
By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Approach - Using Priority Queue
Intuition
The problem revolves around scheduling tasks efficiently while maintaining a cooling period between identical tasks. 
To optimize the total time taken to execute all tasks, we need to minimize the idle time spent waiting for the cooling period to elapse.

Approach
We first count the frequency of each task using a Counter.
We create a max heap to store the negative counts of tasks. Negative counts are used to simulate a max heap as Python's heapq library by default implements a min heap.
We iterate over the tasks and populate the max heap with the negative counts of each task.
We initialize a variable time to keep track of the total time elapsed.
We use a deque q to store pairs of [-count, idleTime]. This deque helps us track the idle time required before a task can be executed again.
We iterate until both the max heap and deque are empty.
Increment the time variable by 1 to simulate the passage of time.
If the max heap is empty, it means there are no pending tasks to execute, so we set the current time to the idle time of the first task in the deque.
If the max heap is not empty:
Pop the most frequent task from the max heap and calculate its new count after execution.
If the count is nonzero, we enqueue it back to the deque along with its idle time (current time + cooling period).
Check if there are any tasks in the deque ready to be executed. If the idle time of the first task in the deque matches the current time, it means the cooling period has elapsed, so we push the task back to the max heap.
Return the total time elapsed.

Complexity

Time complexity:
Constructing the max heap takes O(n log k), where n is the number of tasks and k is the number of distinct tasks.
The while loop iterates at most n times.
Inside the loop, operations like heap push, pop, and deque operations take O(log k) time.
Overall, the time complexity is O(n log k).

Space complexity:
We use a max heap and a deque, each potentially storing at most k elements, where k is the number of distinct tasks.
Thus, the space complexity is O(k).

'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        count = Counter(tasks)
        # Initialize a max heap with negative counts
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Total intervals
        time = 0
        # Deque to store the char and its idle time for controlling the cooling period 
        d = deque()
        while maxHeap or d:
            time += 1

            if not maxHeap:
                # When the max heap is empty time will be taken as the time of first char of queue
                time = d[0][1]
            
            else:
                cnt = 1 + heapq.heappop(maxHeap)  # Will be adding maxFreq char, so 1 + getMaxFreqChar
                
                # If cnt is zero, the char is completely used, so no need to add to deque
                if cnt:  
                    d.append([cnt, time+n])  # We are enqueing cnt and the idle time
            
            if d and d[0][1] == time:  # If the cooling period is done for the first char of deque, add it again into heap
                heapq.heappush(maxHeap, d.popleft()[0])
        
        return time


'''

Approach - Greedy Algorithm

Let's suppose the maximum frequency (number of occurrences) of the task/character in string ‘tasks’ is ‘maxFreq’ and the number of tasks with that maximum frequency is ‘countMaxFreq’. 
We have ‘n’ tasks and a ninja wants at least ‘t’ unit of time between any two same tasks.    

Now, we can make a ‘maxFreq-1’ group of the size ‘t’+1 ( the last group will not contain idle spaces, it will contain the tasks with maximum frequency only). 
Each group has a different task with maximum frequency and the remaining number of empty slots i.e ‘_’ (if there is less than ‘t’+1 such task). 
The total length of these ‘maxFreq’ groups will be (‘maxFreq’-1)*(t+1) + ‘countMaxFreq’. Here, ‘countMaxFreq’ tells the size of the last group. 
Note, the units of time required is equal to the total length of these ‘maxFreq’ groups.

For example, Let there be two tasks ‘A’ and ‘B’ having maximum frequency 3. And ‘t’ = 2.

Then, we can arrange these tasks in order  AB_AB_AB, where _ represent the time when a ninja is idle. Since the maximum frequency of a task (in this case ‘A’ and ‘B’) is 3, there will be 3 groups. 
The size of the first two groups will be equal to ‘t’+1, which is 3 ( denoting (AB_)(AB_)). 
The last group won’t contain the idle spaces and will only contain the characters left which are the characters with maximum frequency, AB in this case, which gives size 2. 
So,it takes takes at least (3-1)*(2+1) + 2 = 8 units of time.

After placing at most ‘t’+1. tasks with the highest frequency, we can place all the remaining tasks in empty slots (the time when a ninja is idle),  
If all the empty slots get filled then we can increase the size of groups. Thus answer will be maximum of ‘n’ and (‘maxFreq’-1)*(t+1) + ‘countMaxFreq’.   
The answer will be ‘n’ when all empty slots get filled

Time Complexity - O(n), where ‘n’ is the number of tasks.
We are doing only a single traversal over string ‘tasks’ of length ‘n’.

Space Complexity - O(c), where ‘c’ is a constant equal to 26.
The space used by array ‘freq’ is a constant equal to 26

'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        ## APPROACH : GREEDY ##
        ## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1
        
        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
                                     # ans   =     rows_except_last   * columns +        last_row
            
            
        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)
        
        
        # Count the frequency of each task
        freq = list(Counter(tasks).values())
        
        # Get the maxFreq char count 
        maxFreq = max(freq)

        # Count the no of chars with maxFreq
        maxFreqCount = freq.count(maxFreq)

        # The maxFreq element will come after every n elements, so multiply maxFreq with n+1
        # The remaining maxFreq chars will be placed at last row so add the maxFreqCount to time
        time = (maxFreq - 1) * (n+1) + maxFreqCount
        
        # For few test cases, time would be less than total len, in that scenario return the len of tasks
        return max(len(tasks), time)
