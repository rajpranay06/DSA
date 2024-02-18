def prefixToInfixConversion(s: str) -> str:
    # Stack for storing the operands.
    st = []

    # Iterating from right to left.
    for i in range(len(s) - 1, -1, -1):
        # Check if the current character is an operator.
        if s[i] in ['+', '-', '*', '/', '^']:
            # Taking last two operands from the stack.
            op1 = st.pop()
            op2 = st.pop()

            # Combining the two operands with the current operator
            # and pushing back to the stack.
            new_top = "(" + op1 + s[i] + op2 + ")"
            st.append(new_top)
        else:
            # Pushing the character s[i] into the stack.
            st.append(s[i])

    # Last operand in the stack will be the final answer.
    return st.pop()
