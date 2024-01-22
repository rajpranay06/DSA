'''

Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.

Input Format:  N = 6, array[] = {11,33,33,11,33,11}
Result: 11 33
Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.

Extended Boyer Moore’s Voting Algorithm: 

Approach: 
Initialize 4 variables:
cnt1 & cnt2 –  for tracking the counts of elements
el1 & el2 – for storing the majority of elements.
Traverse through the given array.
If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.
If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.
If the current element and el1 are the same increase the cnt1 by 1.
If the current element and el2 are the same increase the cnt2 by 1.
Other than all the above cases: decrease cnt1 and cnt2 by 1.
The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).

'''

class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        count1, count2 = 0, 0
        ele1, ele2 = None, None

        # applying the Extended Boyer Moore’s Voting Algorithm:
        for i in a:
            if count1 == 0 and i != ele2:
                count1 += 1
                ele1 = i
            elif count2 == 0 and i != ele1:
                count2 += 1
                ele2 = i
            elif i == ele1:
                count1 += 1
            elif i == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []  # list of answers

        # Manually check if the stored elements in
        # el1 and el2 are the majority elements:
        cnt1, cnt2 = 0, 0
        for i in a:
            if ele1 == i:
                cnt1 += 1
            if ele2 == i:
                cnt2 += 1
                
        k = len(a)//3 + 1
        if cnt1 >= k:
            res.append(ele1)
        if cnt2 >= k:
            res.append(ele2)

        # Uncomment the following line
        # if it is told to sort the answer array:
        # res.sort() #TC --> O(2*log2) ~ O(1);
      
        return res


'''

Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the counts and find the expected majority elements. The second one is to check if the calculated elements are the majority ones or not.

Space Complexity: O(1) as we are only using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.

'''
