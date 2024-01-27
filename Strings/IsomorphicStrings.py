'''

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "paper", t = "title"
Output: true

Input: s = "bbbaaaba", t = "aaabbbba"
Output: false

The approach is to maintain a mapping between characters in both strings and check if the mapping is consistent throughout the strings. 
The mapping is done using the index variable, and each character is associated with a unique index in the mapping arrays.
If at any point, the mappings are not consistent, the function returns false. Otherwise, it returns true at the end.

'''

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str1_hash = defaultdict(lambda: 0)
        str2_hash = defaultdict(lambda: 0)
        for i in range(len(s)):
            if str1_hash[s[i]] != str2_hash[t[i]]:
                return False
            str1_hash[s[i]] = i+1
            str2_hash[t[i]] = i+1
        return True

'''

Time Complexity - O(N)
Space Complexity - O(N) + O(N)

'''
