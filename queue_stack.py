# implementation of queue using stack

import collections
class MyQueue:

    def __init__(self):
        self.s = collections.deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.popleft()

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        return False
