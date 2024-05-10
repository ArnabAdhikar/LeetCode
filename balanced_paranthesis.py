# implementing balanced paranthesis

def isValidParenthesis(s: str) -> bool:
    # open bracket-> push
    # closing bracket-> pop
    temp = []
    for i in s:
        if i in ['(','{','[']:
            temp.append(i)
        else:
            if temp:
                top = temp[-1]
                if ((top == '(' and i == ')') or (top == '[' and i ==']') or (top =='{' and i == '}')):
                    temp.pop()
                else:
                    return False
            else:
                return False
    if len(temp)==0:
        return True
    else:
        return False
