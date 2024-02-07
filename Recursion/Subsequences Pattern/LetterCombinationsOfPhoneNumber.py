'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res=[]

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Recursive function
        def visit(idx, s):

            if idx==len(digits):
                res.append(s)
                return
            
            # Getting the alphabets of the number
            val = phone[digits[idx]]

            for c in val:
                visit(idx+1, s+c)
        
        # Function call
        visit(0, "")
        return res
