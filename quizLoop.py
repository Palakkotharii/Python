"""Create a new list in that there may strign , number s , etc but you have to print only the number swhich are greater than 6."""

items = [int, float,"Rishi",5,3,3,22,21,64,23,233,23]

for item in items:
    if str(item).isnumeric() and item>6: #The python isnumeric() method expects a string and checks if the characters in the string are numeric.
        print(item)