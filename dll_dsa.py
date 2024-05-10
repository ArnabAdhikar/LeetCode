# doubly linked list.
class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class Linkedlist:
    global count
    count = 1

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        global count
        count += 1

    def print_ll(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        global count
        count += 1

    def pop(self):
        try:
            temp = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            self.length -= 1
            global count
            count -= 1
        except:
            print("The list is now empty...")

    def prepend(self):
        a = int(input("Number = "))
        new_node = Node(a)
        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.head = self.tail = new_node
        else:
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        '''global count
        count +=1'''

    def pop_first(self):
        try:
            temp = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                temp.next = None
                self.head.prev = None
            self.length -= 1
            global count
            count -= 1
        except:
            print("The list is empty...")

    def get(self):
        """
        try:
            temp = self.head
            ind = int(input("Enter the index number = "))
            for i in range(ind):
                temp = temp.next
            print("Data = ", temp.value)
        except:
            print("Something went wrong...")
        optimizing the code
        """
        try:
            ind = int(input("Enter the index number = "))
            print(self.length)
            if ind < self.length / 2:
                temp = self.head
                for i in range(ind):
                    temp = temp.next
            else:
                temp = self.tail
                for i in range(self.length - 1, ind, -1):
                    temp = temp.prev
            print("Data = ", temp.value)
        except:
            print("Something went wrong...")

    def set_value(self):
        try:
            ind = int(input("Enter the index number = "))
            val = int(input("Enter the value = "))
            if ind < self.length / 2:
                temp = self.head
                for i in range(ind):
                    temp = temp.next
                temp.value = val
            else:
                temp = self.tail
                for i in range(self.length - 1, ind, -1):
                    temp = temp.prev
                temp.value = val
        except:
            print("Something went wrong...")

    def insert(self):
        try:
            ind = int(input("Enter the index number = "))
            if ind == 0:
                self.prepend()
            elif ind == self.length():
                val = int(input("Enter the value = "))
                self.append(val)
            else:
                val = int(input("Enter the value = "))
                new_node = Node(val)
                bef = self.head
                aft = bef.next
                for i in range(ind):
                    bef = bef.next
                    aft = aft.next
                new_node.prev = bef
                new_node.next = aft
                bef.next = new_node
                aft.prev = new_node
            self.length += 1
        except:
            print("Something Went wrong...")

    def remove(self):
        ind = int(input("Enter the index number : "))
        try:
            if ind == 0:
                temp = self.head
                if self.length == 1:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    temp.next = None
                    self.head.prev = None
                self.length -= 1
                global count
                count -= 1
            elif ind == self.length - 1:
                temp = self.tail
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    temp.prev = None
                self.length -= 1
            else:
                temp = self.head
                for i in range(ind):
                    temp = temp.next
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                temp.next = None
                temp.prev = None
                self.length -= 1
        except:
            print("Something went wrong...")


print("Operations (Doubly Linked List)->")
print("1. Append")
print("2. Pop")
print("3. Prepend")
print("4. Pop First")
print("5. Get")
print("6. Set Value")
print("7. Insert")
print("8. Remove")
print("9. Display")
print("10. Quit")
while True:
    a = int(input("Enter your choice : "))
    if a == 1:
        b = int(input("Number = "))
        if count == 1:
            global my_ll
            my_ll = Linkedlist(b)
        else:
            my_ll.append(b)
    elif a == 2:
        my_ll.pop()
    elif a == 3:
        my_ll.prepend()
    elif a == 4:
        my_ll.pop_first()
    elif a == 5:
        my_ll.get()
    elif a == 6:
        my_ll.set_value()
    elif a == 7:
        my_ll.insert()
    elif a == 8:
        my_ll.remove()
    elif a == 9:
        my_ll.print_ll()
    elif a == 10:
        break
    else:
        print("Wrong input...")
