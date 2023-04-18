#  Write a program to print if the given number is zero or odd or even.
number = int(input("Enter a number : "))
if number==0:
    print("Given number is Zero")
elif number%2==0:
    print("Given number is Even")
else:
    print("Given number is Odd")