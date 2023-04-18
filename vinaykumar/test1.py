# write a program to print the grade of a student based on the marks obtained. 
marks = int(input("Enter marks :"))
if marks>90:
    print("Outstanding")
elif marks>80:
    print("A+ Grade")
elif marks>70:
    print("A Grade")
elif marks>60:
    print("B Grade")
elif marks>50:
    print("C Grade")
elif marks>40:
    print("Pass")
else:
    print("Fail")