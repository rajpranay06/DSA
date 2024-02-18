'''

Problem statement
You are given a string denoting a valid Postfix expression containing ‘+’, ’-’, ’*’, ‘/’ and lowercase letters.

Convert the given Postfix expression into a Prefix expression.

Note:
Postfix notation is a method of writing mathematical expressions in which operators are placed after the operands. For example, "a b +" represents the addition of a and b.

Prefix notation is a method of writing mathematical expressions in which operators are placed before the operands. For example, "+ a b" represents the addition of a and b.

Expression contains lowercase English letters, ‘+’, ‘-’, ‘*’, and  ‘/’. 

'''

def preToPost(s: str) -> str:

    st = []

    for i in range(len(s)-1,-1,-1):
        if s[i] in ['+', '-', '*', '/', '^']:
            new_top = st.pop() + st.pop() + s[i]
            st.append(new_top)
        else:
            st.append(s[i])
    
    return st.pop()
