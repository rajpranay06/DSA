'''

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Optimised  Approach 1

Approach: We will have two pointers left and right. Pointer ‘left’ is used for maintaining the starting point of the substring while ‘right’ will maintain the endpoint of the substring.
'right' pointer will move forward and check for the duplicate occurrence of the current element if found then the ‘left’ pointer will be shifted ahead so as to delete the duplicate elements.

Time Complexity: O( 2*N ) (sometimes left and right both have to travel a complete array)
Space Complexity: O(N) where N is the size of HashSet taken for storing the elements

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        n = len(s)
        hashSet = []
        for r in range(n):
            while l < r and s[r] in hashSet:
                hashSet.pop(0)
                l += 1
            
            hashSet.append(s[r])
            maxLen = max(maxLen, r-l+1)
        
        return maxLen


'''

Optimised  Approach 2

Approach: In this approach, we will make a map that will take care of counting the elements and maintaining the frequency of each and every element as a unity by taking the latest index of every element.

Time Complexity: O( N )
Space Complexity: O(N) where N represents the size of HashSet where we are storing our elements

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = 0
        n = len(s)
        hashMap = {}
        
        for r in range(n):
            # Set the left pointer to the last repeated index
            if s[r] in hashMap:
                l = max(l, hashMap[s[r]] + 1)
            hashMap[s[r]] = r
            maxLen = max(maxLen, r-l+1)
            
        return maxLen
