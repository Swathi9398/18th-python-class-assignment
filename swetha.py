1. write a program to print the grade of a student based on the marks obtained. 
  marks=int(input("enter marks:")
  if marks>=91:
            print("A+ grade")
  elif marks<=90 and marks>=81:
            print("A grade")
  elif marks<=80 and marks>=71:
            print("B+ grade")
  elif marks<=70 and marks>=61
            print("B grade")
  elif marks<=60 and marks>=51:
            print("C+ grade")
  elif marks<=50 and marks>=41:
            print("C grade")
  else:
            print("Fail")
            
      
2. Write a program to print if the guven year is leap or not.
      year=int(input("enter a year")
      if year%4==0 and (year%100!=0 or year%400==0):
               print(year,"is a leap year")
      else:
               print(year,"is not a leap year")
3. Write a program to print if the given number is zero or odd or even.
      num=int(input("enter a number:"))
      if num==0:
               print("zero")
      elif num%2==0:
               print("even")
      else:
               print("odd")
               
               
4. Write a program to check the strength of a password.(please provide different rules for the password)
      pwd=input("enter a password:")
      lcase="abcdefghijklmnopqrstuvwxyz"
      ucase=lcase.upper()
      digits="0123456789"
      symbols=",.!@#$%^&*(){}[];:"'<>?"
      if len(pwd)<8:
               print("password is weak") 
      elif not any(char in lcase for char in pwd):
               print("password needs a lowercase character")
      elif not any(char in ucase for char in pwd):
               print("password needs a uppercase letter")
      elif not any(char in digits for char in pwd):
               print("password needs a digit")
      elif not any(char in symbols for char in pwd):
               print("password need a symbol")
      else:
               print("password is strong")
            
                     
                
               
5.Write a program to create a calculator that perform basic arithematic operations.
       num1=int(input("Enter a number"))
       num2=int(input("enter a number"))
       op=input("enter the operator:"))
       match op:
            case '+':
                  print("addition:",num1+num2)
            case '-':
                  print("subtraction:",num1-num2)
            case '*':
                  print("multiplication:",num1*num2)
            case '/':
                  print("division:",num1/num2)
            case _:
                  print("invalid operation")
            
