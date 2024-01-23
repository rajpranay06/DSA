'''

Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

Each student gets at least one book.
Each book should be allocated to only one student.
Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

Observations:


Minimum possible answer: We will get the minimum answer when we give n books of the array to n students(i.e. Each student will receive 1 book). 
Now, in this case, the maximum number of pages will be the maximum element in the array. So, the minimum possible answer is max(arr[]).
Maximum possible answer: We will get the maximum answer when we give all n books to a single student. The maximum no. of pages he/she will receive is the summation of array elements i.e. sum(arr[]). 
So, the maximum possible answer is sum(arr[]).

From the observations, it is clear that our answer lies in the range [max(arr[]), sum(arr[])].

'''

def allocatePages(a,pages):
    noOfStudents = 1
    currentBook = 0
    for i in a:
        if currentBook + i <= pages:
            # add pages to current student
            currentBook += i
        else:
            # add pages to next student
            noOfStudents += 1
            currentBook = i
    if pages == 71:
        print(noOfStudents)
    return noOfStudents
  
def findPages(a: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    if m > n:
        return -1
    low = max(a)
    high = sum(a)
    while low <= high:
        mid = (low+high)//2
        if allocatePages(a,mid) <= m:
            high = mid - 1
        else:
            low = mid + 1
    return low

'''

Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. 
Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.

'''
