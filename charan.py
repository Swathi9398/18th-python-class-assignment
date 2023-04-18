1. write a program to print the grade of a student based on the marks obtained. 
2. Write a program to print if the guven year is leap or not.
3. Write a program to print if the given number is zero or odd or even.
4. Write a program to check the strength of a password.(please provide different rules for the password)
5.Write a program to create a calculator that perform basic arithematic operations.


/////
1.
marks=int(input("Enter marks of the student"))
if(marks>90 and marks<=100):
  print("Grade:O(Outstanding")
elif(marks>84 and marks<=90):
  print("Grade:A+")
elif(marks>78 and marks<=84):
  print("Grade:A")
elif(marks>70 and marks<=78):
  print("Grade:B")
elif(marks>60 and marks<=70):
  print("Grade:C")
elif(marks>50 and marks<=60):
  print("Grade:D")
elif(marks>45 and marks<=50):
  print("Grade:E")
elif(marks>40 and marks<=45):
  print("Grade:Pass")
elif(marks>0 and marks<=40):
  print("Grade:Fail")
else:
  print("Marks are Invalid")
  
  
/////
2.


year=int(input("Enter any year to check if it is leap year(or)not"))
if(year%100==0):
  if(year%400==0):
    print("The given year {} is leap year".format(year))
  else:
    print("The given year {} is not a leap year".format(year))
else:
  if(year%4==0):
    print("The given year {} is leap year".format(year))
  else:
    print("The given year {} is not a leap year".format(year))
    
  
//////


3.
number=int(input("Enter any number"))
if(number==0):
  print("Given number is Zero")
elif(number%2==0):
  print("Given number is Even")
elif(number%2!=0):
  print("Given number is Odd")
else:
  print("Given number is not an integer")
  
 
//////

4.
print("To create a password follow the given rules")
print("  1.The length of the password should be atleast 12 characters")
print("  2.A combination of uppercase letters, lowercase letters, numbers, and symbols.")
print("  3.Not a word that can be found in a dictionary or the name of a person, character, product, or organization.")
pass=input("Based on the above criteria,Enter your password")
has_upper=false
has_digit=false
has_special=false
has_lower=false
lst="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(len(pass)):
  if(pass[i].islower()):
      has_lower=true
  if(pass[i].isupper()):
      has_upper=true
  if(pass[i].isdigit()):
      has_digit=true
  if(pass[i] not in lst):
      has_special=true
if(has_lower and has_upper and has_special and has_digit):
  print("The password is strong")
elif(has_lower and has_upper and has_digit or has_special):
  print("The password is moderate")
else:
  print("The password is weak")
  
/////


5.

print("Choose any one of the Arthematic operations provided below to perform")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.Modulo")
c=int(input("select the operations from 1 to 5"))
a=int(input("Enter the 1st value:"))
b=int(input("Enter the 2nd value:"))
if(c==1):
  print("Addition of {} and {} is {}".format(a,b,a+b))
elif(c==2):
  print("Subtraction of {} and {} is {}".format(a,b,a-b))
elif(c==3):
  print("multiplication of {} and {} is {}".format(a,b,a*b))
elif(c==4):
  if(b!=0):
     print("Division of {} and {} is {}".format(a,b,a/b))
  else:
     print("Division by zero is not possible")
elif(c==5):
  print("Remainder of {} divided by {} is {}".format(a,b,a%b))
else:
  print("Enter valid choice")

