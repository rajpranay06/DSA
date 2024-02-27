'''

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Intuition
When approaching this problem, the key insight lies in recognizing the significance of character frequencies. 
The solution hinges on maintaining a balance between the window size and the maximum count of any character within that window. 
The primary challenge is to ensure that the number of characters that need to be replaced to form a valid substring doesn't exceed the given limit, k. 
The focus is not on the characters themselves, but rather on their frequency and distribution within the current window. 
A common pitfall to avoid is mistakenly decrementing the count of the wrong character when shrinking the window. 
It's crucial to remember that we only need to adjust the count of the character at the start index of our window, as we are effectively narrowing down the window size.

Approach
The approach involves using a sliding window technique with a hash map (hasho) to track the frequency of characters in the current window. 
We iterate over the string, expanding the window by adding characters and updating their frequency. The variable most_frequent keeps track of the count of the most frequent character in the window. 
If the condition (window size - most_frequent) > k is met, it signifies that more than k replacements are needed to make the substring valid. 
In such a case, we shrink the window from the left by reducing the count of the character at the start index and moving the start index to the right, by one step. 
The maximum length of a valid substring is updated throughout the iteration.

Complexity
Time complexity: The time complexity is O(n), as the algorithm involves a single pass through the string, where n is the length of the string.
Space complexity: The space complexity is O(1), as the hash map will contain at most 26 entries (assuming the input string contains only uppercase English letters).

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        left, right, n = 0, 0, len(s)
        mostFreq, maxLen = 0, 0
        for right in range(n):
            # Setting the frequency of chars
            h[s[right]] = h.get(s[right], 0) + 1
            
            # Getting the mostFreq char from the window
            mostFreq = max(mostFreq, h[s[right]])
            winLen = right - left + 1

            # Get no of replacements, if no of replacements > k shrink the window
            if winLen - mostFreq > k:
                h[s[left]] -= 1
                left += 1
            else:
                # Get the maxLen
                maxLen = max( maxLen, winLen)
        
        return maxLen

