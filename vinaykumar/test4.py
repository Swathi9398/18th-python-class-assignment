#  Write a program to check the strength of a password.(please provide different rules for the password)
password = input("Enter password: ")
numbers = 1
lower_case = 1
upper_case = 1
special_charactetr = 1
for i in password:
    if i.isdigit():
        numbers = 0
    if i.islower():
        lower_case = 0
    if i.isupper():
        upper_case = 0
    if i in "!@#$%^&*()-+":
        special_charactetr = 0
count = len(password)
if count<8 or numbers or lower_case or upper_case or special_charactetr:
    print("PASSWORD is WEAK")
    print("a password must contain minimum of 8 characters, ONE UpperCase, ONE LowerCase,ONE Digit and ONE Special Character")
else:
    print("password is strong")