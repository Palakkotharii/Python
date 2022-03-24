# list1 = ("Harry", "Larry", "Marry", "Cherry")

list1 =[ ["Harry",1], ["Larry",1], ["Marry",2],
        ["Cherry",6], ["Marry",250]]

# print(list1[0], list1[1])

"""
for item in list1:
    print(item)
"""

for item, lollypop in list1:
    print(item, "and lolly is ", lollypop)
    
# type casting the dictionary :

dict1 = dict(list1)
print(dict1)

for item, lollypop in dict1.items(): # items() method is used to return the list with all dictionary keys with values. as  dictionary holds key : value pair.
    print(item, "and lolly is ", lollypop)

for item in dict1:
    print(item) # this will print only the keys :