'''

Problem statement
You are given an integer array 'a' of size 'n'.
For each element in the array, check whether the immediate right element of the array is smaller or not.
If the next element is smaller, update the current index to that element. If not, then -1. The last element does not have any elements on its right.

Example :
Input: 'a' = [4, 7, 8, 2, 3, 1]

Output: Modified array 'a' = [-1, -1, 2, -1, 1, -1]

Explanation: In the array 'a':
4 has 7 on its right. Since 7 is not smaller, we update 4 to -1.
7 has 8 on its right. Since 8 is not smaller, we update 7 to -1.
8 has 2 on its right. Since 2 is smaller than 8, we update 8 to 2.
2 has 3 on its right. Since 3 is not smaller, we update 2 to -1.
3 has 1 on its right. Since 1 is smaller than 3, we update 3 to 1.
1 does not have any element on right. So we update 1 to -1.

Approach 1 - Using Stack

The idea is to traverse the array and store the just previous element of the current element in a data structure, say Stack, and then compare its top with the next element

Initialize the stack ‘s’ to store the previous element that is a[i - 1] for a[i].
Push the first element of a to s.
Now run a loop from index i = 1  till the end of the array and check for each element if(s.peek() > a[i]).
If the conditions satisfy, update a[i - 1] as a[i].
Else put a[i - 1] = -1
Now push the current element for the next iteration.
Finally, in the update a[n - 1] = -1 because there are no further elements to check.

Time Complexity - O(n), Where ‘n’ denotes the number of elements in the array
We are traversing the array once to find the final array that takes O(n) time. Hence, the overall Time Complexity is O(n).

Space Complexit - O(n), Where ‘n’ denotes the number of elements in the array.
The Space Complexity O(n) is required for Stack to store elements.  Hence, the overall Space Complexity is O(n).

'''

from typing import List

def immediateSmaller(a: List[int]) -> None:
    # Write your code here
    n = len(a)

    # Use a deque to store previous element.
    stack = []
    stack.append(a[0])

    for i in range(1, n):
        # If the top is greater than the current element, then copy the current element to previous.
        if stack[-1] > a[i]:
            a[i - 1] = a[i]
        else:
            # Else, set it to -1.
            a[i - 1] = -1

        # Push the current element to the stack for the next iteration.
        stack.append(a[i])

    # Finally, for the last element, put it as -1.
    a[n - 1] = -1


'''

Approach 2 - Without using extra space
The idea is to traverse the array and just check the next element with the current element.

Run a loop from index 0 to n - 2 (inclusive) and check for each element if (a[i + 1] > a[i])
If the conditions satisfy, update a[i] TO a[i + 1]
Else put a[i] = -1
Finally, in the update a[n - 1] = -1 because there are no further elements to check.

Time Complexity - O(n), Where ‘n’ denotes the number of elements in the array
We are traversing the array once to find the final array that takes O(n) time. Hence, the overall Time Complexity is O(n).

Space Complexity - O(1).
We are using constant space. Hence, the overall Space Complexity is O(1).


'''

from typing import List

def immediateSmaller(a: List[int]) -> None:
    # Write your code here
    n = len(a)
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i] = a[i+1]
        else:
            a[i] = -1
    
    a[n-1] = -1
