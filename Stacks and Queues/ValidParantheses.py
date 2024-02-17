'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''

class Solution:
    def isValid(self, s: str) -> bool:
        charMap = { "}":"{",  "]":"[",  ")":"(" }
        stack = []

        for c in s:
            if c in charMap:
                if stack and stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

'''

Time Complexity: O(N)
Space Complexity: O(N)

'''

