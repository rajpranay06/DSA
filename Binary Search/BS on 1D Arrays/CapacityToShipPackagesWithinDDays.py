'''

You are the owner of a Shipment company. You use conveyor belts to ship packages from one port to another. The packages must be shipped within ‘d’ days.
The weights of the packages are given in an array ‘of weights’. The packages are loaded on the conveyor belts every day in the same order as they appear in the array. 
The loaded weights must not exceed the maximum weight capacity of the ship.
Find out the least-weight capacity so that you can ship all the packages within ‘d’ days.

Observation:


Minimum ship capacity: The minimum ship capacity should be the maximum value in the given array. Let’s understand using an example. 
Assume the given weights array is {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} and the ship capacity is 8. 
Now in the question, it is clearly stated that the loaded weights in the ship must not exceed the maximum weight capacity of the ship. 
For this constraint, we can never ship the weights 9 and 10, if the ship capacity is 8. 
That is why, in order to ship all the weights, the minimum ship capacity should be equal to the maximum of the weights array i.e. nax(weights[]).
Maximum capacity: If the ship capacity is equal to the sum of all the weights, we can ship all goods within a single day. Any capacity greater than this will yield the same result. 
So, the maximum capacity will be the summation of all the weights i.e. sum(weights[]).

From the observations, it is clear that our answer lies in the range
[max(weights[]), sum(weights[])]

'''

class Solution:
    def countDays(a,k,cap):
        day = 1   # First day
        s = 0
        for i in a:
            if s + i > cap:
                day += 1   # Move to next day
                s = i
            else:
                # Load the weight on the same day
                s += i
        return day <= k
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low+high)//2
            if Solution.countDays(weights,days,mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

'''

Time Complexity: O(N * log(sum(weights[]) – max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
Reason: We are applying binary search on the range [max(weights[]), sum(weights[])]. For every possible answer ‘mid’, we are calling findDays() function. 
Now, inside the findDays() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''
