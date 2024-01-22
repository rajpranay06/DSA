'''

Intuition

In this approach, we intend to get rid of two things i.e. the HashSet we were using for the look-up operation and the set data structure used to store the unique triplets.

So, We will first sort the array. Then, we will fix a pointer i, and the rest 2 pointers j and k will be moving. 

Now, we need to first understand what the HashSet and the set were doing to make our algorithm work without them. 
So, the set data structure was basically storing the unique triplets in sorted order and the HashSet was used to search for the third element.

That is why, we will first sort the entire array, and then to get the unique triplets, we will simply skip the duplicate numbers while moving the pointers.

How to skip duplicate numbers:
As the entire array is sorted, the duplicate numbers will be in consecutive places. So, while moving a pointer, we will check the current element and the adjacent element. 
Until they become different, we will move the pointer by 1 place. We will follow this process for all 3 pointers. Thus, we can easily skip the duplicate elements while moving the pointers.

Now, we can also remove the HashSet as we have two moving pointers i.e. j and k that will find the appropriate value of arr[j] and arr[k]. So, we do not need that HashSet anymore for the look-up operations.

1. If the sum is greater, then we need lesser elements and so we will decrease the value of k(i.e. k–). 
2. If the sum is lesser than the target, we need a bigger value and so we will increase the value of j (i.e. j++). 
3. If the sum is equal to the target, we will simply insert the triplet i.e. arr[i], arr[j], arr[k], into our answer and move the pointers j and k skipping the duplicate elements.

'''

class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        res = []
        a.sort()
        n = len(a)

        for i in range(n):

            # remove duplicates:
            if i != 0 and a[i] == a[i-1]:
                continue

            # moving 2 pointers:
            j = i+1
            k = n-1
            while j < k:
                s = a[i] + a[j] + a[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    temp = [a[i],a[j],a[k]]
                    res.append(temp)
                    j += 1
                    k -= 1

                    # skip the duplicates:
                    while j < k and a[j] == a[j-1]:
                        j += 1
                    while j < k and a[k] == a[k+1]:
                        k -= 1
        return res


'''

Time Complexity: O(NlogN)+O(N2), where N = size of the array.
Reason: The pointer i, is running for approximately N times. And both the pointers j and k combined can run for approximately N times including the operation of skipping duplicates. 
So the total time complexity will be O(N2). 

Space Complexity: O(no. of quadruplets), This space is only used to store the answer. We are not using any extra space to solve this problem. 
So, from that perspective, space complexity can be written as O(1).

'''
                     
