def infixToPostfix(exp: str) -> str:
    # Write your code here.
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3,'(':0}
    stack = []
    postfix_out = ""
    for i in exp:
        if i=="(":
            stack.append(i)
        elif i==")":
            while stack[-1]!="(":
                postfix_out = postfix_out+stack.pop()
            stack.pop()
        # i->incomming
        elif i in precedence:
            while stack and precedence[stack[-1]]>=precedence[i]:
                postfix_out = postfix_out+stack.pop()
            stack.append(i)
        else:
            postfix_out+=i
    # for the other elements in the stack
    while stack:
        postfix_out+=stack.pop()
    return postfix_out
