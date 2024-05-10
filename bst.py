# implementing binary search tree.
# all the operations are included.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Bst:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    def search(self, value1):
        if self.root is None:
            return False
        else:
            temp1 = self.root
            while temp1 is not None:
                if value1<temp1.value:
                    temp1 = temp1.left
                elif value1>temp1.value:
                    temp1 = temp1.right
                else:
                    return True     # value is present.
            return False      # value is not present.
    def min_val(self):
        temp2=self.root
        while temp2.left is not None:
            temp2 = temp2.left
        return temp2.value
    def max_val(self):
        temp3 = self.root
        while temp3.right is not None:
            temp3 = temp3.right
        return temp3.value
a = Bst()
print("All the choices :->")
print("1. Insert.")
print("2. Search.")
print("3. Minimum Value.")
print("4. Maximum Value")
print("5. End")
while True:
    n = int(input("Enter your choice : "))
    if n==1:
        b = int(input("Enter the number : "))
        a.insert(b)
    elif n==2:
        b = int(input("Enter the number : "))
        print("Result : ", a.search(b))
    elif n==3:
        print(a.min_val())
    elif n==4:
        print(a.max_val())
    elif n==5:
        break
    else:
        print("Enter a good choice...")
print("Now displaying some of the element :--->>>")
try:
    print(a.root.value)            
    print(a.root.left.value)        
    print(a.root.right.value)
except:
    print("NoneType object has no attribute 'value'")