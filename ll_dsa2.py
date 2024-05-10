class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
ll = Linkedlist(4)
print(ll.head.value)    # accessing the value
