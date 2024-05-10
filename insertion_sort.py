# implementing insertion sort.
def in_sort(lst):
    for i in range (1,len(lst)):
        temp = lst[i]
        j = i-1
        while temp < lst[j] and j>-1:
            lst[j+1] = lst[j]
            lst[j] = temp
            j-=1   # for shifting j to the previous position.
    return lst
a = eval(input("Enter the list : "))
print("The sorted list : ",in_sort(a))
