# performing bubble sort
def bubble (lst):
	for i in range (len(lst)-1,0,-1):
		for j in range (i):
			if lst[j]>lst[j+1]:
				temp=lst[j]
				lst[j]=lst[j+1]
				lst[j+1]=temp
	return lst
a = eval(input("Enter the list : "))
print("list = ", bubble(a))
