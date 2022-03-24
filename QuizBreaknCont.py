"""Take input from user until and unless it becomes greater than 100"""

i=0
while (True):
    inp = int(input("Enter a number :  \n"))
    if inp > 100:
        print("Congrats you have entered a number greater than 100 \n")
        break
    else:
        print("Try Again \n")
        continue
    
    