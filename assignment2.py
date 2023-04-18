students_marks=int(input("Enter a value:"))
if (students_marks>=80 and students_marks<=100):
  print("A grade")
elif students_marks>=70 and students_marks<=79:
  print("B grade")
elif students_marks>=60 and students_marks<=69:
  print("c grade")
elif students_marks>=40 and students_marks<=59:
  print("D grade")
else:
 print("Fail")
#######



year=int(input("Enter a year:"))
if((year%4==0) and (year%400==0 or year%100!=0)):
  print("Leap year")
else:
  print("Not a Leap year")
######



number=int(input("Enter a number"))
if number==0:
  print("Zero")
elif number%2==0:
  print("Number is a Even")
else:
  print("Number is a Odd")
########



a=int(input("Enter a value"))
b=int(input("Enter a value"))
class Calculator:
    def add(a,b):
        print("Addition:",a+b)
    def sub(a,b):
        print("Subtraction:",a-b)
    def mul(a,b):
        print("Multiplication:",a*b)
    def div(a,b):
        print("Division:",a/b)
c=Calculator
c.add(a,b)
c.sub(a,b)
c.mul(a,b)
c.div(a,b)
#########


def passw(password):
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    specialchar = any(c in "!@#$%^&*()" for c in password)

    if (length and uppercase and lowercase and digit and specialchar):
        print("Strong Password")
    elif length and digit and specialchar:
        print("Moderate Password")
    else:
        print("Weak Password")
password=input("Enter password: ")
passw(password)

