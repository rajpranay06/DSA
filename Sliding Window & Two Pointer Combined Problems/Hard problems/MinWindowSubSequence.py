'''

You are given two strings ‘S’ and ‘T’. Your task is to find the minimum (Contiguous) substring ‘W’ of ‘S’, such that ‘T’ is a subsequence of ‘W’
A subsequence is a sequence that can be derived from another sequence by removing zero or more elements, without changing the order.
A substring is a contiguous part of a string.

For example:
For the given string “CodingNinjas”: “Ninja” is a substring while “dinas” is a subsequence. 
If there is no such Window in ‘S’ that covers all characters in ‘T’, return an empty string "". If there are multiple such minimum length windows, return the one with the smallest starting index.

Sample Input 1 :
2
rdew
u
abcdebdde
bde

Sample Output 1 :
""
bcde

Explanation For Sample Output 1 :

For test case 1 :
Since there is no window in ‘S’ which covers all characters of ‘T’ so therefore we returned an empty string.

For test case 2 :
“bcde” is the substring of minimum length in which we find “bde”. “bdde” is also a substring of minimum length however the index of “bcde” occurs first, therefore we returned bcde

Two Pointer Approach

We will find the window where we can actually find the whole string ‘T’. Then after that, since we have to return the minimum length window, we will try to shrink this window as much as possible. 

The steps are as follows :

Maintain 2 pointers i,j and initialize them to 0. Position of i indicates string ‘S’ and position of ‘J’ indicates ‘T’
Whenever S[i] == T[j], then move both the pointers ahead, otherwise move only i pointer ahead.
When the value of j becomes equal to T.size(), then we know that we have finally found our string ‘T’ in string ‘S’. Now it’s time to shrink this window.
Before shrinking let us understand why there are redundant characters that can be removed.
Each time we were increasing the ith pointer in the starting.
For example, let us consider the following strings, where S = “abcdebdde”, and T = “bde”.
abcdebdde              bde
    ^(i)                 ^(j)

In this case, our pointers are as shown. Initially, we took the letter ‘a’ as an extra letter that can be removed. So, therefore, in order to remove these extra characters, we will again go in reverse order until j>=0. Covering the whole pattern again backwards will definitely produce the minimum window possible. We will mark the current position of i as ‘End’.
Now after traversing backward, our pointers will look like
abcdebdde              bde
^(i)                  ^(j)

When j finally reach the starting point, we realized that the whole pattern is traversed, and the length of the minimum window is end-i.
We will repeat this process again for the rest of our string, and update our current minimum.

Time Complexity - O(N^2), where N is the length of string ‘S’
As we are first moving forward, and then backwards. At ith iteration, in the worst case, we might have to traverse the string till the end. 
So at each index, if we are traversing the whole string again, complexity will be O(N ^ 2)

Space Complexity - O(1)
We have not used any extra space.

'''

def minWindow(s, t):
    # write your code here
    if not s or not t or len(s) < len(t):
        return ""
    # Map storing ASCII values as index of alphabets
    index, right, start_index = 0, 0, 0
    minL = float('inf')
    
    while right < len(s):
        # If index of char in t is present in s char go to next index
        if s[right] == t[index]:
            index += 1
        
        # if all the char of t is in s
        while index >= len(t):
            # Set the end of substring
            end = right
            index -= 1
            # Shrink the window from right till index = -1
            while index >= 0:
                # Decrementing the index and comapring chars in t and s from back
                if s[right] == t[index]:
                    index -= 1
                right -= 1
            
            # Will be out of bound, so add 1 to each
            index += 1
            right += 1

            # Set the start_index and minLen
            if minL > end - right:
                minL = end - right
                start_index = right
            
        right += 1
    
    # If all characters of t are not in s
    if minL == float("inf"):
        return ""
    else:
        return s[start_index: start_index+minL+1]

    
