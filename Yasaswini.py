1. write a program to print the grade of a student based on the marks obtained.
marks = int(input("Enter the marks obtained by a student : "))
if marks >= 90 and stu_marks <=100 :
    print("grade = A+")
elif marks  >= 80:
    print("grade = A")
elif marks  >= 70:
    print("grade = "B")
elif marks >= 60:
    print(grade = C")
elif marks  >= 50:
    print("grade = D")
elif marks<=50 and stu_marks>0:
    print("grade = F")
else:
  print("Invalid marks")



2. Write a program to print if the given year is leap or not.
year=int(input("Enter any year to check it is leap year or not: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap year")
else:
    print("Not a leap year")
          
3. Write a program to print if the given number is zero or odd or even.
num = int(input("Enter a number: "))
if num == 0:
    print("The given number is zero")
elif num % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

4. Write a program to check the strength of a password.(please provide different rules for the password)
print("The password should be at least 10 characters long.")
print("The password should contain at least one uppercase letter.")
print("The password should contain at least one lowercase letter.")
print("The password should contain at least one digit.")
print("The password should contain at least one special character")
password = input("Enter a password: ")
l1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',', '.', '?', ':', '{', '}', '|', '<', '>']
strength_value = 0
if len(password) >= 10:
    strength_value+= 1
if any(char.isupper() for char in password):
    strength_value += 1
if any(char.islower() for char in password):
   strength_value+= 1
if any(char.isdigit() for char in password):
    strength_value += 1
   for char in password:
         if char in l1:
            strength_value += 1
            break;

if strength_value == 5:
    print("Password is very strong.")
elif strength_value >= 3:
    print("Password is strong.")
elif strength_value >= 1:
    print("Password is weak.")
else:
    print("Password is very weak.")
          
5.Write a program to create a calculator that perform basic arithematic operations.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif operator == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operator == "/":
        result = num1 / num2
        print(num1, "/", num2, "=", result)
elif operator == "%":
          result = num1 % num2
          print(num1, "%", num2, "=", result)
else:
    print("Invalid operator")
