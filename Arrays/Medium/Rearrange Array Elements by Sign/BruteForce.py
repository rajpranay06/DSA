'''

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Approach:
In this simple approach, since the number of positive and negative elements are the same, we put positives into an array called “pos” and negatives into an array called “neg”.
After segregating each of the positive and negative elements, we start putting them alternatively back into array A.
Since the array must begin with a positive number and the start index is 0, so all the positive numbers would be placed at even indices (2*i) and negatives at the odd indices (2*i+1), 
where i is the index of the pos or neg array while traversing them simultaneously.
This approach uses O(N+N/2) of running time due to multiple traversals which we’ll try to optimize in the optimized approach given below.

'''

def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []
  
    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
  
    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]
  
    return A

# Array Initialisation.
A = [1, 2, -4, -5]
ans = rearrange_by_sign(A)

for i in range(len(ans)):
    print(ans[i], end=" ")


'''

Time Complexity: O(N+N/2) { O(N) for traversing the array once for segregating positives and negatives and another O(N/2) for adding those elements alternatively to the array, 
where N = size of the array A}.

Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.

'''

