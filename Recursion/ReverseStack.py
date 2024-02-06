'''

Problem statement
Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.

Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

Example:
Input: [1,2,3,4,5] 
Output: [5,4,3,2,1]

'''

def reverse(s, a):
    if not s:
        for i in a:
            s.append(i)
        return 
    
    a.append(s.pop())
    reverse(s,a)
    

def reverseStack(s: List[int]) -> None:
    # Write your code here.
    if not s:
        return

    reverse(s, [])

    return s
