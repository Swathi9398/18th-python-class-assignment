##grades
a=int(input("enter marks : "))
if a>=91 and a<=100:
    print("Your Grade is A+")
elif a>=81 and a<91:
    print("Your Grade is A")
elif a>=71 and a<81:
    print("Your Grade is B+")
elif a>=61 and a<71:
    print("Your Grade is B")
elif a>=51 and a<61:
    print("Your Grade is C+")
elif a>=41 and a<51:
    print("Your Grade is C")
elif a>=31 and a<41:
    print("Your Grade is D+")
elif a>=21 and a<31:
    print("Your Grade is D")
else:
    print("Failed the test!")
    
##leapyear
year = int(input("Enter year : "))
if (year % 400 == 0 and year % 100 == 0):
    print(" year is leap year")
elif (year % 4 ==0 and year % 100 != 0):
    print("year is leap year")
else:
    print("year is not leap year")

##0 or odd or even
a=int(input("Enter a number : "))
if(a==0):
    print(a)
if(a%2 == 0):
    print("even")
else:
    print("odd")
    
##strong password
length = lower = upper = digit = special = False
password = input("Enter password: ")

if (len(password) > 7):
    length = True
    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
if length and lower and upper and digit:
    print("Strong Password")
else:
    print("Weak Password")

    
# basic calculator operations
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
operation = input("Enter the operator :")
if (operation == '+'):
    print(a + b)
elif (operation == '-'):
    print(a - b)
elif (operation == '*'):
    print(a * b)
elif (operation == '/'):
    print(a / b)
else:
    print('not a valid operator')
