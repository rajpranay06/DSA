'''

You are given ‘N’ roses and you are also given an array ‘arr’  where ‘arr[i]’  denotes that the ‘ith’ rose will bloom on the ‘arr[i]th’ day.
You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly ‘k’ adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least ‘m’ bouquets each containing ‘k’ roses. Return -1 if it is not possible.

Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

Observation: 


Impossible case: To create m bouquets with k adjacent flowers each, we require a minimum of m*k flowers in total. 
If the number of flowers in the array, represented by array-size, is less than m*k, it becomes impossible to form m bouquets even after all the flowers have bloomed. 
In such cases, where array-size < m*k, we should return -1.

Maximum possible answer: The maximum potential answer corresponds to the time needed for all the flowers to bloom. In other words, it is the highest value within the given array i.e. max(arr[]).
Minimum possible answer: The minimum potential answer corresponds to the time needed for atleast one flower to bloom. In other words, it is the smallest value within the given array i.e. min(arr[]).

Note: From the above observations, we can conclude that our answer lies between the range [min(arr[]), max(arr[])].

'''

class Solution:
    def checkBouquets(a,k,x):
        c = 0
        res = 0

        # count the number of bouquets
        for i in a:
            if i <= x:
                c += 1
            else:
                res += (c//k)
                c = 0
        res += (c//k)
        return res
    def minDays(self, a: List[int], m: int, k: int) -> int:
        if len(a) < m*k:
            return -1   # impossible case
        low = min(a)
        high = max(a)
        noOfB = 0
        ans = max(a)
        while low <= high:
            mid = (low+high)//2
            noOfB = Solution.checkBouquets(a,k,mid)
            #print(noOfB,mid)
            if noOfB < m:
                low = mid + 1
            else:
                high = mid - 1
                ans = min(mid,ans)
        return ans


'''
Time Complexity: O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
Reason: We are applying binary search on our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer ‘mid’, we will call the possible() function. 
Inside the possible() function, we are traversing the entire array, which results in O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''
