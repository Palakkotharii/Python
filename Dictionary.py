print("Welome to the Dictionary in python")
# dictionary is nothing but key value pairs

""" Remember !!
[] => this is for the list
() => this is for the tuple
{} => this is for the dictionary

"""


d1 = {}
# print(type(d1)) # this is the declaration of the dictionary

d2 = {"Palak": "Pizza", "Rohan": "Burger", "Priyansh": "Chocolate",
      "Shubham": {"B": "maggie", "L": "roti", "d": "Chinnese"}}
# d2["Ankit"] ="Junk Food"
# print(d2)
# print(d2["Palak"]) # this will print the value of Palak
# print(d2["Shubham"])
# print(d2["Shubham"]["B"]) # jo hamari dictionary ki value hai vo list,tuple , dictionary bhi ho skti hai but the keys are Immutable
# d2[420] ="Kebabs"
# print(d2)
# del d2[420] # this delets the 420


# Functions in the Dictionary
# 1. Copy()
# d3=d2 # yahapr copy nhi ban rhi hai orignal reference hi ja rha hai
d3 = d2.copy()
del d3["Palak"]
print(d2)
print(d3)

# 2) get fn
print(d2.get("Palak"))

# 3) update fn
d2.update({"Urfi": "DIY"})
print(d2)

# 4) key() => to print all the keys
print(d2.keys())

# 5) items => print the key value pairs
print(d2.items())
