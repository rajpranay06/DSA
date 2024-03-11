'''

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true


Approach 1: Using two stacks

The approach is to record the index of either left bracket or star character in separate stacks, and then when encountering a right bracket, 
attempt to match it with a corresponding left bracket, star, or failing that, to return false.
Once the string has been fully evaluated in the for loop, remaining elements in both stacks are evaluated against each other.
If the index of the left bracket is less than that of the star, they can be matched together and eliminated.
Finally, if there are any remaining elements in the left bracket stack, we can surmise there were insufficient stars to neutralize all remaining left brackets.
If there are no remaining elements, the stars and left brackets were evenly matched.

Time Compelxity - O(N)
Space Complexity - O(N)

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftBracketStack = []
        starStack = []
        # Add index of ( and * into their stack
        for i in range(len(s)):
            if s[i] == "(":
                leftBracketStack.append(i)
            elif s[i] == '*':
                starStack.append(i)
            else:
                # When ), check first if leftBracketStack has any indices next starStack
                if leftBracketStack:
                    leftBracketStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        
        # For remaining leftBracket and star stack indices
        while leftBracketStack and starStack:
            left = leftBracketStack.pop()
            star = starStack.pop()

            # If left is present after *, theri would be no right paranthesis to make it valid
            if left > star:
                return False
        
        # If left stack is empty then only it is a valid paranthesis
        return not leftBracketStack


'''

Approach 2:

1. Have two counters one counter (cmax) for counting the maximum number of right braces we can accommodate with current left braces and stars. 

2. Have a second counter(cmin) which represents the minimum number of right braces that must be there further to make sure the whole string is valid(this number can’t be negative, 
so if it becomes negative then we put it to zero. 

3. At any time, if cmax becomes negative, it means we can’t accommodate current right braces with current left braces and stars. So, we return false. 

4. In the end if cmin is positive then it means that at least there should be a cmin number of right braces to make sure the overall string is valid. 
So, we check whether cmin is zero or not and return the answer 


There are two conditions in which the string is unbalanced
1. We encounter too many ')'
2. In the end, we still have some '(' which didn't find their matching ')'

cmax takes care of condition 1
cmax represents the number of ')' we MIGHT encounter. For cmax, we treat '*' as '('
So at any point of time, if cmax becomes negative, that means, with all the '(' and '*' we have encountered, there are more ')'. 
So return false
Note that we only worry about extra ')' 

cmin takes care of condition 2
cmin represents the number of ')' we MUST encounter. So the job of cmin is to get to 0 as quickly as possible
For cmin, we will always assume that '*' is a ')'. So whenever we encounter ')' or '*', we reduce cmin.
But, cmin can not go below 0. If this happens, we can assume few of the '*'s as empty.
Don't worry about a condition like ()))) because we have cmax which takes care of this.
We only worry about extra '('
So at the end, if cmin is still > 0, this means, with all the '*' and ')' we encountered, there are more '(' present in the string
So return false

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for c in s:
            if c == '(':
                cmin += 1
                cmax += 1
            elif c == ')':
                cmin -= 1
                cmax -= 1
                if cmax < 0:   # // Currently, don't have enough open parentheses to match close parentheses-> Invalid
                    return False  #  For example: ())(
                if cmin < 0:
                    cmin = 0  # It's invalid if open parentheses count < 0 that's why cmin can't be negative
            else:
                cmax += 1  # if `*` become `(` then openCount++
                cmin -= 1  # if `*` become `)` then openCount--
                # if `*` become `` then nothing happens
                # So openCount will be in new range [cmin-1, cmax+1]
                if cmin < 0:
                    cmin = 0
        
        return cmin == 0 # Return true if can found `openCount == 0` in range [cmin, cmax]  
            
'''

Time Complexity - O(N)
Space Complexity - O(1)

'''
