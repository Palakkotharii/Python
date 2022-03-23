print("Welcome to the List in the python!!")

# grocery =["Harpic", "vim bar", "deodrant", "Bindi","Loolypop",56]
# print(grocery)  this is to print the full of the list!!!

#  accessing the values from  the List 
"""print(grocery[0])
print(grocery[1])
print(grocery[2])
print(grocery[3])
"""
"""
numbers = [2,7,9,11,3]
print("The original numebers are :", numbers)
numbers.sort() # here this will change the original list!!
print("Sorted number list is :", numbers)

numbers.reverse() # here this will change the original list
print("Numbers after reversing the whole list are :", numbers)
"""

"""
# Slicing in the list [slicing returns the new list but if we do the operations like reverse, sort then original string is changed]
numbers = [2,7,9,11,3]
print(numbers[:])
print(numbers[0:4])
print(numbers[:4])
print(numbers[0:4]) 
"""

# Extended Slicing 
numbers = [2,7,9,11,3]
print(numbers[::])
print(numbers[::2]) # ye 1 jan koskip marega
print(numbers[::2]) # if we take the negative values then it will  reverse list and then if first 2 values are the default then only it will work !!

# function in list :
print("length of the number is :",len(numbers)) 
print("Maximum of the number is :",max(numbers)) 
print("Minimum of the number is :",min(numbers)) 

# append() => means end me jod do yarr !!
# numbers.append(7)
# print(numbers)
""" You can use like this also above append function !!
numbers= []
numbers.append(7)
numbers.append(3)
numbers.append(2)
print(numbers)
"""

""" if you want to insert some values at the middle or anywhere you can you the insert() function!!

numbers.insert(1,34)
print(numbers)
"""

# remove function 
"""numbers.remove(11)
print(numbers)
"""
# pop function => removes the last element from the list!!x
numbers.pop()
print(numbers)

