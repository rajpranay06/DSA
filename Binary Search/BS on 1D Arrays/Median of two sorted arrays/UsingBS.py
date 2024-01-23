'''

A median divides array into two equal halves. Try to select elements from arr1 and arr2 and take it as 2 halves selected elements from arr1 and arr2 would be of one half and the remaining would be second half. 
Check if the divided halves are valid or not. By assigning variables l1 and r1 to last elements of arr1 and arr2 of left half. 
And l2 and r2 for first elements of arr1 and arr2 of right half. If l1 <= r2 and r1 <= l2 the halves are valid and return (max(l1,r1)+min(l2,r2))/2. 

'''

class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        m,n = len(a1), len(a2)
        if m > n:
            return self.findMedianSortedArrays(a2,a1)
        l = (m+n+1)//2
        low = 0
        high = m
        while low <= high:
            cut1 = (low+high)//2
            cut2 = l - cut1
            l1,l2,r1,r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if cut1 < m:
                r1 = a1[cut1]
            if cut2 < n:
                r2 = a2[cut2]
            if cut1 - 1 >= 0:
                l1 = a1[cut1 - 1]
            if cut2 - 1 >= 0:
                l2 = a2[cut2 - 1]

            if l1 <= r2 and l2 <= r1:
                if (m+n)%2 == 1:
                    return max(l1,l2)
                return ((max(l1,l2)) + min(r1,r2))/2
            
            if l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return 0

'''

Time Complexity: O(log(min(n1,n2))), where n1 and n2 are the sizes of two given arrays.
Reason: We are applying binary search on the range [0, min(n1, n2)].

Space Complexity: O(1) as no extra space is used.

'''
