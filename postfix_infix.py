def postToInfix(postfix: str) -> str:
    # Write your code here.
    stack = []
    for i in postfix:
        if i.isalpha():
            stack.append(i)
        else:
            # operator
            A = stack.pop()
            B = stack.pop()
            stack.append('('+B+i+A+')')
    return stack[0]
