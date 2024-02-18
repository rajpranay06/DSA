'''

Problem statement
You are given a mathematical expression in postfix notation. The expression consists of alphabets(both lowercase and uppercase) and operators.

Convert this expression to infix notation.

Note:
Surround every expression with a pair of parentheses “()”.

Example:
Input: ‘postfix’ = “ab+c+”
Output: ‘infix’ = “((a+b)+c)”

Explanation: The expression ((a+b)+c)” in infix is equivalent to “ab+c+” in postfix.


'''

def postToInfix(postfix: str) -> str:
    # Write your code here.
    st = []
    for i in postfix:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i >= '0' and i <= '9'):
            st.append(i)
        else:
            if st:
                second = st.pop()
                first = st.pop()
                new_top = '(' + first + i + second + ')'
                st.append(new_top)
    
    return st.pop()

