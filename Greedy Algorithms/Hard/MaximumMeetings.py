'''

There is one meeting room in a firm. You are given two arrays, start and end each of size N.For an index ‘i’, 
start[i] denotes the starting time of the ith meeting while end[i]  will denote the ending time of the ith meeting. 
Find the maximum number of meetings that can be accommodated if only one meeting can happen in the room at a particular time. 

Example:

Input:  N = 6,  start[] = {1,3,0,5,8,5}, end[] =  {2,4,5,7,9,9}

Output: 4

Initial Thought Process:-
Say if you have two meetings, one which gets over early and another which gets over late. Which one should we choose?  If our meeting lasts longer the room stays occupied and we lose our time. 
On the other hand, if we choose a meeting that finishes early we can accommodate more meetings. Hence we should choose meetings that end early and utilize the remaining time for more meetings.

Approach: 

To proceed we need a vector of three quantities: the starting time, ending time, meeting number. Sort this data structure in ascending order of end time. 
We need a variable to store the answer. Initially, the answer is 1 because the first meeting can always be performed. Make another variable, say limit that keeps track of the ending time of the meeting that was last performed. Initially set limit as the end time of the first meeting

Start iterating from the second meeting. At every position we have two possibilities:-

If the start time of a meeting is  strictly greater than limit we can perform the meeting. Update the answer.Our new limit is the ending time of the current meeting  since it was last performed.
Also update limit.  
If the start time is less than or equal to limit , skip and move ahead. 

'''

from typing import List

def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    
    # Add start end and its pos into a list
    a = []
    for i in range(len(start)):
        a.append([start[i], end[i], i+1])
    
    # Sort the array w.r.t end time
    a.sort(key=lambda x: (x[1], x[2]))
    
    # First meeting is always held
    res = 1
    limit = a[0][1]
    for i in range(1, len(a)):
        # If start time is greater than the limit we can perform the meeting
        if a[i][0] > limit:
            limit = a[i][1]
            res += 1
    return res

'''

Time Complexity: O(n) to iterate through every position and insert them in a data structure. O(n log n)  to sort the data structure in ascending order of end time. 
O(n)  to iterate through the positions and check which meeting can be performed.
Overall : O(n) +O(n log n) + O(n) ~O(n log n)

Space Complexity: O(n)  since we used an additional data structure for storing the start time, end time, and meeting no.

'''
