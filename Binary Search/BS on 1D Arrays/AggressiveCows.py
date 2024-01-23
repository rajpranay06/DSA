'''

You are given an array ‘arr’ of size ‘n’ which denotes the position of stalls.
You are also given an integer ‘k’ which denotes the number of aggressive cows.
You are given the task of assigning stalls to ‘k’ cows such that the minimum distance between any two of them is the maximum possible.
Find the maximum possible minimum distance.

Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result: 3
Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. 
Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.

Observation:


Minimum possible distance between 2 cows: The minimum possible distance between two cows is 1 as the minimum distance between 2 consecutive stalls is 1.
Maximum possible distance between 2 cows: The maximum possible distance between two cows is = max(stalls[])-min(stalls[]). This case occurs when we place 2 cows at two ends of the sorted stalls array.

From the observations, we can conclude that our answer lies in the range 
[1, max(stalls[])-min(stalls[])].

'''

def canWePlace(a,dist,cows):
    n = len(a)
    cntCows = 1   # no. of cows placed
    last = a[0]   # position of last placed cow
    for i in range(1,n):
        if a[i] - last >= dist:
            cntCows += 1  # place next cow
            last = a[i]   # update the last location
        if cntCows >= cows:
            return True
    return False
def aggressiveCows(a, k):
    # Write your code here.
    a.sort()
    low = 1
    high = a[-1] - a[0]
    while low <= high:
        mid = (low+high)//2
        if canWePlace(a,mid,k):
            low = mid+1
        else:
            high = mid - 1
    return high

'''

Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
Reason: O(NlogN) for sorting the array. We are applying binary search on [1, max(stalls[])-min(stalls[])]. Inside the loop, we are calling canWePlace() function for each distance, ‘mid’. 
Now, inside the canWePlace() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''
