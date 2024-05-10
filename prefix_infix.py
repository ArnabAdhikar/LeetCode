def prefixToInfixConversion(s: str) -> str:
    stack = []
    # looping through the string in the reverse order
    for i in s[::-1]:
        if i.isalpha():
            stack.append(i)
        else:
            x = stack.pop()
            y = stack.pop()
            stack.append('('+x+i+y+')')
    return stack[0]
