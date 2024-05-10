# performing the selection sort.
def selection(lst):
    for i in range(len(lst)-1):   # traversing the list length-1 times
        ind = i                   # it stores the index of minimum number
        for j in range(i+1,len(lst)):
            if lst[ind]>lst[j]:
                ind = j
        if i!=ind:               # the elements are already sorted
            temp = lst[i]
            lst[i] = lst[ind]
            lst[ind] = temp
    return lst
a = eval(input("Enter the list : "))
print ("The sorted list : ",selection(a))
