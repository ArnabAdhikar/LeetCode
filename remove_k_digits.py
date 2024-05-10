class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monotonic_stack = []
        for i in num:
            while k>0 and monotonic_stack and monotonic_stack[-1]>i:
                k-=1
                monotonic_stack.pop()
            monotonic_stack.append(i)
        # removing the last k digits
        monotonic_stack = monotonic_stack[0:len(monotonic_stack)-k]
        answer = "".join(monotonic_stack)
        if answer:
        # eleminating all the leading 0, if any
            return str(int(answer))
        else:
            return "0"
