'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''

class Solution:
    res = []
    def validParanthesis(left, right, s, n):

        if len(s) == n*2:
            Solution.res.append(s)
            return
        
        if left < n:
            Solution.validParanthesis(left+1,right,s+"(",n)
        
        if right <  left:
            Solution.validParanthesis(left,right+1,s+")",n)


    def generateParenthesis(self, n: int) -> List[str]:

        Solution.res = []

        Solution.validParanthesis(0,0,'',n)

        return Solution.res
        
