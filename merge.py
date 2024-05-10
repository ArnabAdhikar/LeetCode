# performing mereged sort.

def merge(l1,l2):
    combined = []
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            combined.append(l1[i])
            i+=1
        else:
            combined.append(l2[j])
            j+=1
    # when second list is empty
    while i<len(l1):
        combined.append(l1[i])
        i+=1
    # when first list is empty
    while j<len(l2):
        combined.append(l2[j])
        j+=1
    return combined
'''
a = eval(input("Enter the first list : "))
b = eval(input("Enter the second list : "))
print("The sorted list : \n", merge(a,b))
'''
