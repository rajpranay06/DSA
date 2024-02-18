'''

Problem Statement: Given an infix expression, Your task is to convert the given infix expression to a postfix expression.

Examples:

Example 1:
Input: a+b*(c^d-e)^(f+g*h)-i
Output: abcd^e-fgh*+^*+i-
Explanation: Infix to postfix

Example 2:
Input: (p+q)*(m-n)
Output: pq+mn-*
Explanation: Infix to postfix


Approach: To convert Infix expression to Postfix
1. Scan the infix expression from left to right. 

2. If the scanned character is an operand, Print it. 

3. Else, 

If the precedence of the scanned operator is greater than the precedence of the operator in the stack or the stack is empty or the stack contains a ‘(‘, push the character into the stack. 
Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. 
4. If the scanned character is an ‘(‘, push it into the stack. 

5. If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, and discard both the parenthesis. 

6. Repeat steps 2-5 until the entire infix expression is scanned. 

7. Print the output.

8. Pop and print the output from the stack until it is not empty.

Time Complexity: O(N)
Space Complexity: O(N) for using the stack

'''

def precedence(c):
    if c == '^':
        return 3
    if c == '*' or c == '/':
        return 2
    if c == '+' or c == '-':
        return 1
    return -1

def infixToPostfix(s: str) -> str:
    # Write your code here.
    st = []
    res = ""
    for i in s:
        # If character or integer add to res
        if (i >= 'a' and i <= 'z') or  (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
            res += i
        
        elif i == "(":
            st.append(i)
        
        elif i == ")":
            while st[-1] != "(":
                res += st.pop()
            
            st.pop()
        
        else:
            # If current operator precedence is less than top stack precedence pop the stack
            while st and precedence(i) <= precedence(st[-1]):
                    res += st.pop()
            
            st.append(i)
    
    # Empty the stack
    while st:
        res += st.pop()
    
    return res
