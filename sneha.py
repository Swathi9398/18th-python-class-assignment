1. #1.write a program to print the grade of a student based on the marks obtained. 
2. Write a program to print if the guven year is leap or not.
3. Write a program to print if the given number is zero or odd or even.
4. Write a program to check the strength of a password.(please provide different rules for the password)
5.Write a program to create a calculator that perform basic arithematic operations.
#write a program to print the grade of a student based on the marks obtained.
marks = int(input("Enter marks of a student : "))
if(marks > 90 and marks <= 100):
          print("A+")
elif(marks > 85 and marks <= 90):
          print("A")
elif(marks >75 and marks <= 85):
          print("B+")
elif(marks > 60 and marks <= 75):
          print("C")
elif(marks > 45 and marks <= 60"):
     print("C+")
elif(marks >= 39 and marks <= 45)
     print("D")
else:
     print("FAIL")
   
#2.write a program to print if the given year is leap year or not.
year = int(input("Enter a year : "))
if(year % 400 ==0 and year % 100 == 0):
         print("Given year is leap year")
elif(year % 4 ==0 and year %100 != 0):
         print("Given year is leap year")
else:
         print("Given year is not a leap year")
     
#3.write a program to print if the number is zero or even or odd.
number = int(input("Enter a number : "))
if(number == 0):
    print("zero")
else:
    if(num %2 == 0):
        print("Even")
    else:
        print("odd")
     
#4.write a program to create a calculator that performs basic arithmetic operations.
num = int(input("Enter a number from 1 to 5 : "))
a=int(input("Enter a value : "))
b=int(input("Enter a value : "))
if(num == 1):
     print("ADDITION",a+b)
elif(num == 2):
     print("SUBTRACTION",a-b)
elif(num == 3):
     print("MULTIPLICATION",a*b)
elif(num == 4):
     print("DIVISION",a/b)
elif(num == 5):
     print("MODULO DIVISION",a%b)
else:
     print("The given number is not valid ") 

     
        
     
