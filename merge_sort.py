# performing merge sort.

from merge import merge
def merge_sort(l1):
    if len(l1)==1:       # when the list has only one element
        return l1
    mid = len(l1)//2
    left = l1[:mid]
    right = l1[mid:]
    # merge only works on sorted list so, left and right has to be broken down
    return merge(merge_sort(left),merge_sort(right))
a = eval(input("Enter the list : "))
print("The sorted list : ", merge_sort(a))
