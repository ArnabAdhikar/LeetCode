# factorial of a number using recursion.
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
a = int(input("Enter the number : "))
print("The factorial of the number : ",fac(a))
