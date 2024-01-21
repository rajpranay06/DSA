'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Optimal Approach(Using Set data structure): 
We will adopt a similar approach to the brute-force method but with optimizations in the search process. Instead of searching sequences for every array element as in the brute-force approach, we will focus solely on finding sequences only for those numbers that can be the starting numbers of the sequences. This targeted approach narrows down our search and improves efficiency.

We will do this with the help of the Set data structure.

How to identify if a number can be the starting number for a sequence:

First, we will put all the array elements into the set data structure.
If a number, num, is a starting number, ideally, num-1 should not exist. So, for every element, x, in the set, we will check if x-1 exists inside the set. :
If x-1 exists: This means x cannot be a starting number and we will move on to the next element in the set.
If x-1 does not exist: This means x is a starting number of a sequence. So, for number, x, we will start finding the consecutive elements.
How to search for consecutive elements for a number, x:

Instead of using linear search, we will use the set data structure itself to search for the elements x+1, x+2, x+3, and so on.

'''

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        if len(a) == 0:
            return 0
        s = set()
        c = 0
        longest = 1
        
        # put all the array elements into set
        for i in a:
            s.add(i)

        # Find the longest sequence
        for i in s:
            # if 'i' is a starting number
            if i-1 not in s:
                # find consecutive numbers
                c = 1
                x = i
                while x+1 in s:
                    c += 1
                    x = x+1
                longest = max(c,longest)
        return longest

'''
Time Complexity: O(N) + O(2*N) ~ O(3*N), where N = size of the array.
Reason: O(N) for putting all the elements into the set data structure. After that for every starting element, we are finding the consecutive elements. 
Though we are using nested loops, the set will be traversed at most twice in the worst case. So, the time complexity is O(2*N) instead of O(N2).

Space Complexity: O(N), as we are using the set data structure to solve this problem.

'''
