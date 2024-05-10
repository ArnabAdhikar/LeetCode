# stack using array

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def size(self):
        return len(self.stack)

# Example usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.stack)  # Output: Stack: [1, 2, 3]

print("Peek:", stack.peek())  # Output: Peek: 3

print("Pop:", stack.pop())    # Output: Pop: 3
print("Stack:", stack.stack)  # Output: Stack: [1, 2]

print("Is Empty?", stack.is_empty())  # Output: Is Empty? False

print("Stack Size:", stack.size())