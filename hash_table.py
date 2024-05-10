# hash table.
class Hashtable:
    def __init__ (self, size=7):
        self.data = [None]*size                 # creating a primary table with all the elements None
    def hash(self, key):                        # like returning an index number for the primary list
        hash_i=0
        for i in key:
            hash_i=(hash_i+ord(i)*23)%len(self.data)   # calculation for the hash table
            # ord is used for getting the ASCII.
        return hash_i
    def set(self, key, value):
        index = self.hash(key)                  # for finding out the index
        if self.data[index]==None:              # checking whether that particular slot==None
            self.data[index]=[]                 # creating an empty list if thar slot don't have any element
        self.data[index].append([key,value])    # else append to the last created list
    def get(self, key):
        index = self.hash(key)
        if self.data[index] is not None:
            for i in range (len(self.data[index])):
                if self.data[index][i][0]==key:
                    # printing out the value
                    return self.data[index][i][1]
                else:
                    return None
        else:
            return None
    # retriving all the keys
    def keys(self):
        keys_ll=[]
        for i in range (len(self.data)):
            if self.data[i] is not None:
                for j in range (len(self.data[i])):
                    keys_ll.append(self.data[i][j][0])
        print(keys_ll)
    def print_t(self):
        for i,val in enumerate(self.data):
            print(i," : ",val)
a = Hashtable()
a.set("Arnab Adhikary",1)
a.set("Raju Charan",45)
a.set("Daniel Blue",145)
print(a.get("Raju Charan"))
print(a.get("Raju"))
a.keys()
# printing the elements
a.print_t()
