marks=[12,12.4 , 13.4 , 15 ,16 , "Palak"]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])


# cannot modify the strings :
# str= "hello"
# print(str)
# str[0]='a'

# Slicing of the strings :
marks= [45,56,34,1,2,4,1]
print(marks[1:4])
print(marks[1:])
print(marks[:5])
print(marks[-3 : -1])

# Methods in List :
# marks.append("Palak")
print(marks)

marks.sort()
print(marks)

# marks.sort(reverse=True)
# print(marks)
# # marks.reverse
# print(marks)

marks.insert(1,2)
print(marks)


marks.remove(1) #this will remvoe the firest occreence in the list
print(marks)

marks.pop(4)
print(marks)