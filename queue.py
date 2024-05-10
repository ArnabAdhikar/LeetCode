# queue
class Node:
   def __init__(self, value):
       self.data = value
       self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            val = self.head.data
            self.head = self.head.next
            return val
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
a = Queue()
print("All the operations:->")
print('1. enqueue')
print('2. dequeue')
print('3. quit')
print("4. display")
while True:
    x = int(input('What operation would you like to perform ? '))
    if x == 1:
        b = int(input("Enter the number = "))
        a.enqueue(b)
    elif x == 2:
        c = a.dequeue()
        if c is None:
            print('The queue is empty.')
        else:
            print('The deleted element is : ', int(c))
    elif x == 3:
        break
    elif x==4:
        a.display()
    else:
        print("Enter a correct choice...")
