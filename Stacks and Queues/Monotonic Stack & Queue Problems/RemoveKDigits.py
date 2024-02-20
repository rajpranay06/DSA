'''

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Approach:
In order to get the smallest possible number, we have to get rid of as many as possible big digits in the most significant places on the left. 
We can use a monotonically increasing stack to help us remove those big digits. When adding a new digit, we check whether the previous one is bigger than the current and pop it out. 
In the end, we concatenate the remaining elements from the stack and return the result.

Time Complexity - O(N)
Space Complexity - O(N)

'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        if len(num) == k:
            return '0'

        for i in num:
            while st and k and st[-1] > i:
                st.pop()
                k -= 1
            
            if st or i != '0':
                st.append(i)
        
        if k:
            st = st[:-k]
        
        return ''.join(st) or '0'

  
