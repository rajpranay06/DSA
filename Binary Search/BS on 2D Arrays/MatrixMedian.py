'''

Problem Statement: Given a row-wise sorted matrix of size r*c, where r is no. of rows and c is no. of columns, find the median in the given matrix.

Assume – r*c is odd

Input: 
r = 3 , c = 3
1 4 9 
2 5 6
3 8 7
Output: Median = 5
Explanation: If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9
So, median = 5

Do BS on limit 1, 10^9. Find mid and check how many elements in the array are <= mid. Use upperbound approach to check this. If the cnt <= (m*n)//2 eliminate left half else right half. Finally return low.

'''

def elementsLessThanOrEqualToMid(a,n,k):
    low = 0
    high = n-1
    for i in range(n):
        mid = (low+high)//2
        if a[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return low

def median(a: [[int]], m: int, n: int) -> int:
    # Write your code here.
    low = 1
    high = 1000000000
    while low <= high:
        mid = (low+high)//2
        cnt = 0
        for i in range(m):
            cnt += elementsLessThanOrEqualToMid(a[i],n,mid)
        if cnt <= (m*n)//2:
            low = mid + 1
        else:
            high = mid - 1
    return low

'''

Time Complexity: O(row*log col) since the upper bound function takes log c time.

Space Complexity: O(1) since no extra space is required.

'''
