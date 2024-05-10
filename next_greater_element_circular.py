from typing import List

def nextGreaterElementII(arr: List[int]) -> List[int]:
    # Write your code here.
    nge_c=[0]*(2*len(arr))
    stack=[]
    length_original=len(arr)
    n = 2*length_original
    # circular list
    for i in range(n-1, -1, -1):
        while len(stack) and stack[-1]<=arr[i%length_original]:
            stack.pop()
        # stack is empty and the element is not found for that element
        if len(stack)==0:
            nge_c[i] = -1
        else:
            # NGE for that element = stack.top()
            nge_c[i] = stack[-1]
        stack.append(arr[i%length_original])
    return nge_c[0:length_original]
