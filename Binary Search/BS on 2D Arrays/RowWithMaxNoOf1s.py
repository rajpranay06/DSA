'''

Problem Statement: You have been given a non-empty grid ‘mat’ with ‘n’ rows and ‘m’ columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
Your task is to find the index of the row with the maximum number of ones.
Note: If two rows have the same number of ones, consider the one with a smaller index. If there’s no row with at least 1 zero, return -1.

Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).

We cannot optimize the row traversal but we can optimize the counting of 1’s for each row.

Instead of counting the number of 1’s, we can use the following formula to calculate the number of 1’s:
Number_of_ones = m(number of columns) – first occurrence of 1(0-based index).

As, each row is sorted, we can find the first occurrence of 1 in each row using any of the following approaches:

lowerBound(1) (ref: Implement Lower Bound)
upperBound(0) (ref: Implement Upper Bound)
firstOccurrence(1) (ref: First and Last Occurrences in Array)

'''

def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

'''

Time Complexity: O(n X logm), where n = given row number, m = given column number.
Reason: We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

Space Complexity: O(1) as we are not using any extra space.

'''
