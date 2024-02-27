'''

Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        res = 0
        n = len(s)
        h = {'a':0, 'b':0, 'c':0}
        for right in range(n):
            h[s[right]] += 1

            # If abc are present atleast once
            while h['a'] > 0 and h['b'] > 0 and h['c'] > 0:
                # The remaining charcters would be valid substrings
                res += n - right
                # Shrinking from left and check if substrings are still valid
                h[s[left]] -= 1
                left += 1
        
        return res

'''

Two Pointers

We will be maintaining three pointers each for characters ‘a’, ‘b’ and ‘c’ i.e ‘aIdx’, ‘bIdx’ and ‘cIdx’ initially initialised to -1 for maintaining the last index of their occurrence.
We will be iterating via ‘i’ from 0 to ‘n’-1. For each ‘i’ we will update the counters depending on the s[i].
Once we update the counters, we have to find the last index we essentially have to include to make a valid substring ending at ‘i’. 
All the substrings before that last index and ending at ‘i’ would be valid.
The last index is nothing but the minimum of all ‘aIdx’, ‘bIdx’ and ‘cIdx’. We will add all the valid substrings ending at ‘i’ to the final answer.

Time Complexity - O(n),  where ‘n’ is the size of the string ’s'.
We are iterating via ‘i’ from 0 to ‘n’-1. Hence the total time complexity for the solution is O(1).

Space Complexity - O(1).
We are not utilising any extra space here, hence the O(1) space complexity.

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        # Initialising index of last occurrence of each character to '-1'.
        aIdx, bIdx, cIdx = -1, -1, -1

        for i in range(n):

            # Updating the index of last occurrence of each character.
            if s[i] == 'a':
                aIdx = i
            elif s[i] == 'b':
                bIdx = i
            else:
                cIdx = i

            minIdx = min(aIdx, bIdx, cIdx)

            # Adding count of all valid substrings.
            ans = ans + (minIdx + 1)

        return ans
