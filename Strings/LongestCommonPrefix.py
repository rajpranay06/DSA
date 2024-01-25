'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Approach:

This code implements the longestCommonPrefix function that takes a list of strings v as input and returns the longest common prefix of all the strings. Here is an explanation of how the code works:

Initialize an empty string ans to store the common prefix.
Sort the input list v lexicographically. This step is necessary because the common prefix should be common to all the strings, 
so we need to find the common prefix of the first and last string in the sorted list.
Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string.
If the current character of the first string is not equal to the current character of the last string, return the common prefix found so far.
Otherwise, append the current character to the ans string.
Return the ans string containing the longest common prefix.
Note that the code assumes that the input list v is non-empty, and that all the strings in v have at least one character. If either of these assumptions is not true, the code may fail.

Time Complexity - O(NlogN) + O(min(len(first), len(last)) 
Space Complexity - O(1)

'''

class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        res = ""
        a.sort()
        for i in range(min(len(a[0]), len(a[-1]))):
            if a[0][i] != a[-1][i]:
                return res
            res += a[0][i]
        return res


