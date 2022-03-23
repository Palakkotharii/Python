from re import A, T


print("Swapping of 2 numbers :")

a=5
print("The first value is :",a)
b=6
print("The Second value is :",b)
"""
temp=a
a=b
b=temp
"""
a,b= b,a # above 3 LOC can be written as follows
print("After swapping the value is :" , end=" ")
print(a,b)
