""" Create  a Dictionary an dtake input from user and retrun the meaning of the words from the dictionary"""


print("This is the homework for dictionary")

dt = {"Borrow" :"take",
     "Academic": "scholastic",
     "Embrace" : "accept",
     "Cognizant" : "awareness ",
     "Phlegmatic" : "expressing little or no emotion"
     }

print("Ente the following to know more: ")
print("Borrow")
print("Academic")
print("Embrace")
print("Cognizant")
print("Phlegmatic")
name =input("Enter the Word :")
print(dt[name])
