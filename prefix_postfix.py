def preToPost(s: str) -> str:
    stack = []
    # looping in the reverse order
    for i in s[::-1]:
        if i.isalpha():
            stack.append(i)
        else:
            # operator
            A = stack.pop()
            B = stack.pop()
            stack.append(A+B+i)
    return stack[0]
