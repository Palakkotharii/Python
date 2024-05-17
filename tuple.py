tup=(1,2,3,4,3)
print(tup)
print(tup[0])
print(type(tup))
tup1=() # this is an empty tuple 
print(tup1)

tup3= ("hello" ,)  # yahapr last me commma hai becoz it will be treated as tuple 
print(type(tup3))

# slicing with tuples :
print(tup[1:3])

# Methods in tuple :
print(tup.index(2))
print("Count of the tuple is : ", tup.count(3))

# Assignment : WAP to ask user to enter names of their 3 favorite  movies and store them in a list :

# mov1= input("Enter the mvovie 1 name :")
# mov2= input("Enter the mvovie 2 name :")        
# mov3= input("Enter the mvovie 3 name :")                                                 
movlist=[]
# movlist.insert(0,mov1)
# movlist.insert(1,mov2)
# movlist.insert(2,mov3)
# print(movlist)


# or :
# movlist.append(mov1)
# movlist.append(mov2)
# movlist.append(mov3)
print(movlist)


# Homework 2 : WAP to check if a list contains a palindrome of elements (use copy )
list=[1,2,3,2,1,] 
list2=list.copy()
print("This is the list 2 :",list2)
list2.reverse()
if list==list2:
    print("Yes it's palindrome ")
else:
    print("No it's  not palindrome")

# WAP to count the nnumber of student with "A" Grade in following tuple 
list6= ["C", "D" , "A" , "A" , "B", "B" , "A"]
print(list6.count("A"))

# WAP to store the above values in list and sort them from "A" to "D"
list7= ["C", "D" , "A" , "A" , "B", "B" , "A"]
list7.sort()
print(list7)