'''
There is an integer array ‘a’ of size ‘n’.
An element is called a Superior Element if it is greater than all the elements present to its right.

You must return an array all Superior Elements in the array ‘a’.

Note:

The last element of the array is always a Superior Element. 

Example

Input: a = [1, 2, 3, 2], n = 4
Output: 2 3

'''

def superiorElements(a : List[int]) -> List[int]:

    # Last element of an array is always a leader,
    # push into ans array.
    res = [a[-1]]
    f = a[-1]
    
    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(len(a)-2,-1,-1):
        if a[i] > f:
            f = a[i]
            res.append(f)
    return res

'''
Time Complexity: O(N) { Since the array is traversed single time back to front, it will consume O(N) of time where N = size of the array }.

Space Complexity: O(N) { There is no extra space being used in this approach. But, a O(N) of space for ans array will be used in the worst case }.
'''
