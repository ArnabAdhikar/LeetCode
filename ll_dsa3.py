# linked list operations.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Linkedlist:
    global count
    count = 1
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length=1
        global count
        count +=1
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        global count
        count +=1
    def print_ll(self):
        temp = self.head
        while temp!=None:
            print(temp.value)
            temp=temp.next
    def pop_ll(self):
        if self.length==0:
            print("The list is empty...")
        else:
            temp=self.head
            pre=self.head
            a = self.tail.value
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail=pre
            self.tail.next = None
            self.length-=1
            global count
            count-=1
            if self.length==0:
                self.head = self.tail = None
        return a
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        global count
        count +=1
    def pop_first(self):
        if self.head==None:
            print("The list is empty...")
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length-=1
        global count
        count-=1
        if self.length==0:
            self.tail=None
    def get(self,index):
        if index<0 or index>self.length:
            print("Index out of range.")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            a=temp.value
        return a
    def set_value(self):
        ind = int(input("Enter the index number = "))
        val = int(input("Enter the value = "))
        if ind<0 or ind>self.length:
            print("Index out of range.")
        else:
            try:
                temp = self.head
                for i in range(ind):
                    temp = temp.next
                temp.value = val
            except:
                print("Something Went Wrong...")
    def insert(self):
        ind = int(input("Enter the index number = "))
        val = int(input("Enter the value = "))
        new_node = Node(val)
        if ind<0 or ind>self.length:
            print("Index out of range.")
        else:
            if ind==0:
                self.prepend(val)
            elif ind==self.length:
                self.append(val)
            else:
                try:
                    temp = self.head
                    for i in range(ind):
                        temp = temp.next
                    new_node.next = temp.next
                    temp.next = new_node
                    self.length-=1
                    global count
                    count-=1
                except:
                    print("Something Went Wrong...")
    def remove(self):
        ind = int(input("Enter the index number = "))
        if ind<0 or ind>self.length:
            print("Index out of range.")
        elif ind==0:
            self.pop_first()
        elif ind==self.length-1:
            self.pop_ll()
        else:
            try:
                prev = self.head
                temp = prev.next
                for i in range(ind-1):
                    prev = prev.next
                    temp = temp.next
                prev.next=temp.next
                temp.next=None
                self.length-=1
                global count
                count-=1
            except:
                print("Something Went Wrong...")
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for i in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
print("Operations :->")
print("1. Append")
print("2. Pop")
print("3. Prepend")
print("4. pop first")
print("5. Get")
print("6. Set value")
print("7. Insert")
print("8. Remove")
print("9. Reverse")
print("10. Display")
print("11. Exit")
while True:
    a = int(input("Enter your choice = "))
    if a==1:
        b = int(input("Number = "))
        if count==1:
            global my_ll
            my_ll=Linkedlist(b)
        else:
            my_ll.append(b)
    elif a==2:
        print("Element popped out : ", my_ll.pop_ll())
    elif a==3:
        b = int(input("Number = "))
        my_ll.prepend(b)
    elif a==4:
        my_ll.pop_first()
    elif a==5:
        b = int(input("Enter the index number = "))
        print("The number against the index : ", my_ll.get(b))
    elif a==6:
        my_ll.set_value()
    elif a==7:
        my_ll.insert()
    elif a==8:
        my_ll.remove()
    elif a==9:
        my_ll.reverse()
    elif a==10:
        my_ll.print_ll()
    elif a==11:
        break
    else:
        print("Wrong choice...")
