'''

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Take stack to store parentheses. If stack is not empty add parentheses to result, then If "(" append to stack else pop the stack. 

'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""

        for char in s:
            if char == "(":
                if stack:
                    res += "("
                stack.append(char)

            else:
                stack.pop()

                if stack:
                    res += char

        return res


'''

Time Complexity - O(n) 
Space Complexity - O(n)

'''
