'''
Approach:

In this optimal approach, we will try to solve the problem in a single pass and try to arrange the array elements in the correct order in that pass only.
We know that the resultant array must start from a positive element so we initialize the positive index as 0 and negative index as 1 and start traversing the array such that whenever we see the first positive element, it occupies the space at 0 and then posIndex increases by 2 (alternate places).
Similarly, when we encounter the first negative element, it occupies the position at index 1, and then each time we find a negative number, we put it on the negIndex and it increments by 2.
When both the negIndex and posIndex exceed the size of the array, we see that the whole array is now rearranged alternatively according to the sign.

'''

def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)
    
    # Define array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans

'''
If the length of pas and neg elements are not same Brute Force approach is only possible.

Time Complexity: O(N) { O(N) for traversing the array once and substituting positives and negatives simultaneously using pointers, where N = size of the array A}.

Space Complexity:  O(N) { Extra Space used to store the rearranged elements separately in an array, where N = size of array A}.

'''
