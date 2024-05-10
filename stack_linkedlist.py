# implementation of stack using linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
    # Write your code here
        self.head = None
        self.capacity = 0
        
    def getSize(self):
        # Write your code here
        return self.capacity

    def isEmpty(self):
        # Write your code here
        if self.head is None:
            return True
        return False

    def push(self, data):
        # Write your code here
        new_node = Node(data)
        if self.isEmpty() is True:
            self.head = new_node
            self.capacity+=1
            return self.head
        itr = self.head
        while itr:
            itr.next=new_node
            new_node.next=None
            self.capacity+=1
            itr = itr.next
        return self.head

    def pop(self):
        # Write your code here
        if self.head is None:
            return False
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.capacity-=1
        return self.head

    def getTop(self):
        # Write your code here
        if self.head is None:
            return False
        return self.head.data
