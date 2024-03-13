'''

We are given two arrays that represent the arrival and departure times of trains that stop at the platform. 
We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

Examples 1:

Input: N=6, 

arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00} 
dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}

Output:3

Explanation: There are at-most three trains at a time. The train at 11:00 arrived but the trains which had arrived at 9:45 and 9:55 have still not departed. So, we need at least three platforms here.

Intuition: At first we need to sort both arrays. When the events will be sorted, it will be easy to track the count of trains that have arrived but not departed yet. 
The total platforms needed at one time can be found by taking the difference between arrivals and departures at that time and the maximum value of all times will be the final answer.

Approach:  At first we need to sort both arrays. When the events will be sorted, it will be easy to track the count of trains that have arrived but not departed yet. 
The total platforms needed at one time can be found by taking the difference of arrivals and departures at that time and the maximum value of all times will be the final answer. 
If(arr[i]<=dep[j]) means if arrival time is less than or equal to the departure time then- we need one more platform. So increment count as well as increment i. 
If(arr[i]>dep[j]) means the arrival time is more than the departure time then- we have one extra platform which we can reduce. So decrement count but increment j. 
Update the ans with max(ans, count) after each iteration of the while loop.

'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(a, d, n):
    # Write your code here.
    a.sort()
    d.sort()
    
    i = 1  # To traverse arrival
    j = 0  # To traverse departure
    platformNeeded = 1
    res = 1

    while i < n and j < n:
        # When arrival is less than or equal to departure we need extra platform
        if a[i] <= d[j]:
            platformNeeded += 1
            i += 1  # Go to next arrival
        else:  
            platformNeeded -= 1
            j += 1  # Train is departured, so go to next train
        res = max(res, platformNeeded)

    return res

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)


'''

Time Complexity: O(nlogn) Sorting takes O(nlogn) and traversal of arrays takes O(n) so overall time complexity is O(nlogn).

Space complexity: O(1)  (No extra space used).

'''
