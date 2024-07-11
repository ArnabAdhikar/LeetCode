class Solution:
    def reverseParentheses(self, s: str) -> str:
        n: int = len(s)
        index_pairs: list[int] = [0 for _ in range(n)]
        stack_start_ind: deque[int] = deque()

        for char_ind in range(n):
            char = s[char_ind]
            if char == "(":
                stack_start_ind.append(char_ind)
            elif char == ")":
                start_ind: int = stack_start_ind.pop()
                index_pairs[char_ind] = start_ind
                index_pairs[start_ind] = char_ind

        res = []
        cur_ind = 0
        cur_dir = 1

        while cur_ind < n:
            char = s[cur_ind]
            if char in "()":
                cur_ind: int = index_pairs[cur_ind]
                cur_dir *= -1
            else:
                res.append(s[cur_ind])
            cur_ind += cur_dir

        return "".join(res)
