class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # hash map
        pairs = {")":"(", "]":"[", "}":"{"}
        # building up the stack
        for c in s:
            # closing parenthesis
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            # opening parenthesis
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
