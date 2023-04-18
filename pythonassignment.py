#1.write a program to print the grade of a student based on the marks obtained
m=int(input("Enter marks")
if m>=90 and m<=80:
      print("A grade")
elif m>=80 and m<=70:
      print("B grade")
elif m>=70 and m<=60:
      print("C grade")
elif m>=60 and m<=50:
      print("D grade")
else:
      print("Fail")
      
#2.write a program to print if the given year is leap year or not
y=int(input("enter a number"))
if y%400==0 and y%100==0:
      print("leap year")
elif y%4==0 and y%100!=0:
      print("leap year")
else:
      print("not a leap year")
     
#3.write a program to print if the given number is zero or odd or even
n=int(input("enter a number"))
if n==0:
      print("zero")
else:
      if n%2==0:
        print("even number")
      else:
        print("odd number")
      
#4.write a program to check the strength of a password
def IsValidPassword(password):
      if(len(password)>5 and len(password)<15):
        lowercase=False
        uppercase=False
        num=False
        special=False
        for char in password:
           if(char.isdigit()):
               num=True
           if(char.islower()):
               lowercase=True
           if(char.isupper()):
               uppercase=True
           if(char.isalnum()):
               special=True
        return lowercase and uppercase and num and special
      else:
         return False
p=input("enter password")
print(IsValidPassword(p))
      
#5.write a program to create a calculator that perform basic arithmetic operations 
def add(a,b):
      return a+b
def sub(a,b):
      return a-b
def mul(a,b):
      return a*b
def div(a,b):
      return a/b
print("p.Add")
print("q.Subtract")
print("r.Multiply")
print("s.Division")
choice=input("enter choice as(p/q/r/s):")
num1=int(input("enter a number"))
num2=int(input("enter a number"))
if choice=='p':
      print(num1,"+",num2,"=",add(num1,num2))
elif choice=='q':
      print(num1,"+",num2,"=",sub(num1,num2))
elif choice=='r':
      print(num1,"+",num2,"=",mul(num1,num2))
elif choice=='s':
      print(num1,"+",num2,"=",div(num1,num2))
else:
      print("Invalid input")


      
      

        
      
