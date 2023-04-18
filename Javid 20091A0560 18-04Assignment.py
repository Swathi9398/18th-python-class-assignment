
#1.
marks = int(input("Enter student marks : "))

if  100   > marks >=92 :
  print("(O) OutStanding")
elif  92   > marks >=85 :
  print("Grade (A+)")
elif  85   > marks >=77 :
  print("Grade (A)")
elif  77   > marks >=68 :
  print("Grade (B)")
elif  68   > marks >=60 :
  print("Grade (C)")
elif  60   > marks >=55 :
  print("Grade (D)")
elif  55   > marks >=40 :
  print("Grade (E)")
elif  40   > marks >=35 :
  print("Pass!")
else :
  print("Fail!")
  
  
#2.

year = int(input("Enter year : "))

if year%100==0 :
  if year%400==0:
    print("Year %d is leap year" %year)
  else :
    print("year %d is not leap year" %year)
elif year%4==0:
  print("year %d is leap year" %year)
else :
  print("year %d is not a leap year" %year)
  
#3.

num = int(input("Enter any integer : "))
if num==0:
  print("Given number is zero")
elif num%2:
  print("Given number ", num ,"is odd")
else :
  print("Given number ", num ,"is even")
  
#4.

print("""
    Please provide the password by following the given below rules.
    1. Password length must be of 12 characters.
    2. Password should contain atleast one lowercase , one uppercase , one number and one special char.
    3. Password should not be same as username or any other organization name.
""")
password = input("Now Enter the password by not voilating the above criteria : ")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

upper = lower = digit = special = False

length = len(password)

for char in password:
  if char.isdigit():
    digit = True
  if char.isupper():
    upper = True
  if char.islower():
    lower = True
  if char not in chars :
    special = True
if special and lower and upper and digit and length==12:
  print("Password is strong")
elif lower and upper or length==12:
  print("Password is Moderate")
else :
  print("Password is weak")

#5 

print("""
    Choose any one of the opertions below
    1. Addition  \t 2. Subtraction \t 3. Multiplication
    4. Division  \t 5. Modulus  \t \t 6. Square Root
    """)

ch = int(input("Enter your choice : "))
def takeInput():
    a , b = map(int , input("Enter two numbers seperated with space : ").split())
    return a,b
if ch==1:
    a,b = takeInput()
    print("Addition of %d and %d is %d" %(a,b,(a+b)))
elif ch==2:
    a,b = takeInput()
    print("Subtraction of %d and %d is %d" %(a,b,(a-b)))
elif ch==3 :
    a,b = takeInput()
    print("Multiplication of %d and %d is %d" %(a,b,(a*b)))
elif ch==4 :
    a,b= takeInput()
    print("Division of %d and %d is %f" %(a,b,(a/b)))
elif ch == 5:
    a,b = takeInput()
    print("Remainder of %d '%' %d is %d" %(a,b,(a%b)))
elif ch == 6 :
    a = int(input("Enter any number : "))
    print("Square root of %d is %f" %(a, a**0.5))
else :
    print("Choose correct operation")
