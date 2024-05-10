class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    global count
    count = 1
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        global count
        count += 1
    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            global count
            count -= 1
        except:
            print("Something went Wrong....")


print("All the operations -> ")
print("1. Push")
print("2. Pop")
print("3. Display")
print("4. Quit")
while True:
    b = int(input("Enter your choice : "))
    if b == 1:
        a = int(input("Number : "))
        if count == 1:
            global my_stack
            my_stack = Stack(a)
        my_stack.push(a)
    elif b == 2:
        my_stack.pop()
    elif b == 3:
        my_stack.print_stack()
    elif b == 4:
        break
    else:
        print("Enter a correct choice...")
