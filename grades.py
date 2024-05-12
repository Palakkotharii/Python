marks= int(input("Enter your marks :"))
if marks>=90:
    grade="A"
elif marks>=80 and marks<=90:
    grade="B"
elif marks>=70 and marks<=80:
    grade="C"
else:
    grade="D"
print("Grade of stident is :" , grade)


# Nesting :
age= 34
if age>=18:
    if age>=80:
        print("Cannot Drive")
    else:
        print("Can drive")
else:
    print("Cannot drive yet")