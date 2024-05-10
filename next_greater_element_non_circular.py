from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    # Write your code here.
    nge = [0]*n
    stack = []
    # not considering the circular array
    for i in range(len(arr)-1, -1, -1):
        # poping out the element from the stack that <= incomming element
        while len(stack) and stack[-1]<=arr[i]:
            stack.pop()
        # stack is empty and the element is not found for that element
        if len(stack)==0:
            nge[i] = -1
        else:
            # NGE for that element = stack.top()
            nge[i] = stack[-1]
        stack.append(arr[i])
    return nge
