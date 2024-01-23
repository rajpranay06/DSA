'''

Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. The median is defined as the middle value of a sorted list of numbers. 
In case the length of the list is even, the median is the average of the two middle elements.

Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
Result: 3.5
Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. 
Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

Merge the two sorted arrays and then find the median in that merged array. 
To optimize the space used in the previous approach, we can eliminate the third array used to store the final merged result. 
After closer examination, we realize that we only need the two middle elements at indices (n1+n2)/2 and ((n1+n2)/2)-1, rather than the entire merged array, to solve the problem effectively.

We will stick to the same basic approach, but instead of storing elements in a separate array, we will use a counter called ‘cnt’ to represent the imaginary third array’s index. 
As we traverse through the arrays, when ‘cnt’ reaches either index (n1+n2)/2 or ((n1+n2)/2)-1, we will store that particular element. This way, we can achieve the same goal without using any extra space.

'''

def median(a, b):
    # size of two given arrays:
    n1, n2 = len(a), len(b)
    n = n1 + n2  # total size
    # required indices:
    ind2 = n // 2
    ind1 = ind2 - 1
    cnt = 0
    ind1el, ind2el = -1, -1

    # apply the merge step:
    i, j = 0, 0
    while i < n1 and j < n2:
        if a[i] < b[j]:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < n1:
        if cnt == ind1:
            ind1el = a[i]
        if cnt == ind2:
            ind2el = a[i]
        cnt += 1
        i += 1
    while j < n2:
        if cnt == ind1:
            ind1el = b[j]
        if cnt == ind2:
            ind2el = b[j]
        cnt += 1
        j += 1

    # Find the median:
    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2.0

'''

Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(1), as we are not using any extra space to solve this problem.

'''
