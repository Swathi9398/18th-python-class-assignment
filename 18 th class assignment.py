#1. write a program to print the grade of a student based on the marks obtained. 

1.
marks=int(input("Enter marks of the student = "))
if(marks>90 and marks<=100):
  print("Grade = O(Outstanding")
elif(marks>82 and marks<=90):
  print("Grade = A+")
elif(marks>74 and marks<=82):
  print("Grade = A")
elif(marks>66 and marks<=74):
  print("Grade = B")
elif(marks>58 and marks<=66):
  print("Grade = C")
elif(marks>50 and marks<=58):
  print("Grade = D")
elif(marks>42 and marks<=50):
  print("Grade = E")
elif(marks>34 and marks<=42):
  print("Grade = Pass")
elif(marks>0 and marks<=34):
  print("Grade = Fail")
else:
  print("Marks are Invalid")
--------------------------------------------------------------------------------------------------------------------------------

#2. Write a program to print if the given year is leap year or not.

year=int(input("Enter the year , which year do you want to check if it leap year or not = "))
if(year%100==0):
  if(year%400==0):
    print("The given year ", year ," is leap year ")
  else:
    print("The given year", year ," is not a leap year")
else:
  if(year%4==0):
    print("The given year", year," is leap year")
  else:
    print("The given year ",year," is not a leap year")
-------------------------------------------------------------------------------------------------------------------------------

#3. Write a program to print if the given number is zero or odd or even.

number=int(input("Enter a number = "))
if(number==0):
  print("Given number is Zero")
elif(number%2==0):
  print("Given number is Even")
elif(number%2!=0):
  print("Given number is Odd")
------------------------------------------------------------------------------------------------------------------------------
  
#4. Write a program to check the strength of a password.(please provide different rules for the password)
print("enter the password based on following  rules")
print("""  1.The length of the password should be atleast 8 characters")
           2.A combination of uppercase letters, lowercase letters, numbers, and symbols .")
           Ex:Kpraveen@123Kumar,K.Har7812@ithA,K.vanI#143hellO  etc;
      """)

password=input("Enter your password = ")
upperletter=false
lowerletter=false
digit=false
symbols=false

comlist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(len(password)):
  if(password[i].islower()):
     lowerletter=true
  if(password[i].isupper()):
      upperletter=true
  if(password[i].isdigit()):
      digit=true
  if(password[i] not in comlist):
      symbols=true
if(lowerletter and upperletter and symbol and digit):
  print("The password is strong")
else:
  print("The password is week")
-------------------------------------------------------------------------------------------------------------------
#5.Write a program to create a calculator that perform basic arithematic operations.

print("Choose any one of the Arthematic operations provided below to perform")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.Modulo division")
c=int(input("select the operations from 1 to 5 = "))
a=int(input("Enter the 1st value = "))
b=int(input("Enter the 2nd value = "))
if(c==1):
  print("Addition of",a," and",b," is ",a+b)
elif(c==2):
  print("Subtraction of ",a," and ",b," is ",a-b)
elif(c==3):
  print("multiplication of ",a," and ",b," is ",a*b)
elif(c==4):
  if(b!=0):
     print("Division of ",a ," and ",b," is ", a/b)
  else:
     print("Division by zero is not possible")
elif(c==5):
  print("Remainder of ",a ," divided by ",b," is ",a%b)
else:
  print("Enter valid choice")
