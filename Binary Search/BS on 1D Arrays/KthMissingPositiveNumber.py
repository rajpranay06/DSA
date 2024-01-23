'''

You are given a strictly increasing array ‘vec’ and a positive integer ‘k’. Find the ‘kth’ positive integer missing from ‘vec’.

Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

	Calculate the missing no of elements at each index by a[i] – (i+1). 
Now do a BS and check for the no of missing elements at mid index. If the missing numbers are < k eliminate left half else right half. Return k + high + 1 as res.

•	So, in the given array, the preceding neighbor of the kth missing number is vec[high]. 
•	Now, we know, up to index ‘high’,
the number of missing numbers = vec[high] - (high+1).
•	But we want to go further and find the kth number. To extend our objective, we aim to find the kth number in the sequence. In order to determine the number of additional missing values required to reach the kth position, we can calculate this as
more_missing_numbers = k - (vec[high] - (high+1)).
•	Now, we will simply add more_missing_numbers to the preceding neighbor i.e. vec[high] to get the kth missing number.
kth missing number = vec[high] + k - (vec[high] - (high+1))
        =  vec[high] + k - vec[high] + high + 1
        = k + high + 1.

'''

class Solution:
    def findKthPositive(self, a: List[int], k: int) -> int:
        low = 0
        high = len(a)-1
        while low <= high:
            mid = (low+high)//2
            missing = a[mid] - (mid+1)
            if missing < k:
                low = mid+1
            else:
                high = mid - 1
        return k + high + 1


'''

Time Complexity: O(logN), N = size of the given array.
Reason: We are using the simple binary search algorithm.

Space Complexity: O(1) as we are not using any extra space to solve this problem.

'''
        
