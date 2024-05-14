class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        def backtrack(openn, closen):
            # base case
            if openn == closen == n:
                res.append("".join(stack))
                return
            # opening parenthesis
            if openn < n:
                stack.append("(")
                backtrack(openn+1, closen)
                # cleanup
                stack.pop()
            # closing parenthesis
            if closen < openn:
                stack.append(")")
                backtrack(openn, closen+1)
                # cleanup
                stack.pop()
        # initially stack is empty
        backtrack(0, 0)
        return res
