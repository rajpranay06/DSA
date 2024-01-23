'''

Observations:

Minimum possible answer: We will get the minimum answer when we place all the gas stations in a single location. Now, in this case, the maximum distance will be 0.
Maximum possible answer: We will not place stations before the first or after the last station rather we will place stations in between the existing stations. 
So, the maximum possible answer is the maximum distance between two consecutive existing stations.
From the observations, it is clear that our answer lies in the range [0, max(dist)].

The traditional binary search algorithm used for integer answer space won’t be effective in this case. 
As our answer space consists of decimal numbers, we need to adjust some conditions to tailor the algorithm to this specific context. The changes are the following:

The traditional binary search algorithm used for integer answer space won’t be effective in this case. 
As our answer space consists of decimal numbers, we need to adjust some conditions to tailor the algorithm to this specific context. The changes are the following:
    •	while(low <= high): The condition ‘while(low <= high)’ inside the ‘while’ loop won’t work for decimal answers, and using it might lead to a TLE error. 
    To avoid this, we can modify the condition to ‘while(high – low > 10^(-6))‘. This means we will only check numbers up to the 6th decimal place. 
    Any differences beyond this decimal precision won’t be considered, as the question explicitly accepts answers within 10^-6 of the actual answer.
    •	low = mid+1: We have used this operation to eliminate the left half. But if we apply the same here, we might ignore several decimal numbers and possibly our actual answer. 
    So, we will use this: low = mid.
    •	high = mid-1: Similarly, We have used this operation to eliminate the right half. But if we apply the same here, we might ignore several decimal numbers and possibly the actual answer. 
    So, we will use this: high = mid.

'''

def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high

'''

Time Complexity: O(n*log(Len)) + O(n), n = size of the given array, Len = length of the answer space.
Reason: We are applying binary search on the answer space. For every possible answer, we are calling the function numberOfGasStationsRequired() that takes O(n) time complexity. 
And another O(n) for finding the maximum distance initially.

Space Complexity: O(1) as we are using no extra space to solve this problem.

'''

