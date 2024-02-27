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
