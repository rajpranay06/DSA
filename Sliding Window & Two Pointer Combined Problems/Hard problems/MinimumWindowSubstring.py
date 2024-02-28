'''

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Intuition
The goal is to find the minimum window in string s that contains all characters from string t. The intuition is to use a sliding window approach with two pointers.

Approach
Initialize a character array map of size 128 to store the frequency of characters in string t.
Initialize variables count, start, end, minLen, and startIndex.
Iterate through each character in string t and update the character frequency in the map.
Use two pointers (start and end) to slide the window and find the minimum window that contains all characters from string t.
Increment end and decrease the frequency in map for each character encountered until all characters from t are present in the window.
When all characters from t are present, update minLen and startIndex based on the current window size and starting index.
Increment start and increase the frequency in map until the window no longer contains all characters from t.
After the iteration, the minimum window is found, and the result is a substring of s starting from startIndex with length minLen.

Complexity
Time complexity: O(n), where n is the length of string s.
Space complexity: O(1), as the map array has a constant size (128).

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        # Map storing ASCII values as index of alphabets
        hashMap = [0]*128
        left, right, start_index = 0, 0, 0
        minL = float('inf')
        charCount = len(t)

        # Get frequency of characters of string t
        for char in t:
            hashMap[ord(char)] += 1
        
        for right in range(len(s)):
            # If the char of s present in t, decrease the charCount
            if hashMap[ord(s[right])] > 0:
                charCount -= 1
            hashMap[ord(s[right])] -= 1

            # If charCount id 0, all characters of t are in s
            while charCount == 0:
                # Set the start_index and minLen
                if minL > right - left + 1:
                    minL = right - left + 1
                    start_index = left
                
                # If char count is 0, the char will not present in next substrings so increase the count 
                if hashMap[ord(s[left])] == 0:
                    charCount += 1
                # Shrink the window from left
                hashMap[ord(s[left])] += 1
                left += 1
            
        # If all characters of t are not in s
        if minL == float("inf"):
            return ""
        else:
            return s[start_index :(start_index + minL)]
