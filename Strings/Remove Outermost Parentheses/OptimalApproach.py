'''

Instead of stack keep a count of parentheses, if “(“ increase the count and if c != 1  add to res. If “)” c--, and if c >= 1 add to res. 

Time Complexity - O(N)
Space Complexity - O(1)

'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c = 0
        res = ""
        for i in s:
            if i == "(":
                c += 1
                if c != 1:
                    res += i
            else:
                c -= 1
                if c >= 1:
                    res += i
        return res
        
