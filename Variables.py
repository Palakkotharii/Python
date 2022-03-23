#python automatically defines the data type !!
a=10
b='Palak'
c=4.99
str1="Palak is Googler "
str2="Priyanshu is my biggest enemy "
str3="99"
str4="1"
print(type(a)) # using this function which tells the dt of variable !!
# print(type(b))
# print(type(c))

print(a+c)
print(str1+str2)

# we can use the int() to convert it into the integer eg:
# we can use the float() to convert it into the float eg:
# we can use the str() to convert it into the string eg:
print("After converting  from string to the integer :=>",int(str3) + int(str4))

# if you want to print hello world 10 times:
# print ( 10 * "Hello world \n")


# taking input from the User !!
print("Enter the number :")
a= input() # remember input function gives only string not an integer !!
print("You entered ",a)
print("After Adding  with 10 you get =>", int(a)+10)

