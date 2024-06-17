class Solution:
    def simplifyPath(self, path: str) -> str:
        # using a stack data structure
        stack = []
        cur = ""
        # trailing / is added for operational convinience
        for c in path+"/":
            if c == "/":
                if cur == "..":
                    # if stack is non empty
                    if stack:
                        stack.pop()
                # multiple slash => cur = ""
                elif cur != "" and cur != ".":
                    stack.append(cur)
                # reset the cur
                cur = ""
            else:
                cur += c
        # stack = ["abc", "def"]
        # joining the stack into a complete string and it should start with /
        return "/"+"/".join(stack)
