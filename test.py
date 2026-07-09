# name="Raju"
# print(name)
# is_logiing  =True
# print(is_logiing)
# name=input("Enter Name : ")

# print(name)

# age=27

# if age>=26:
#     print("Adult")
# else:
#     print("Baby")

# pin = 1234
# balance = 5000

# entered_pin = int(input("Enter PIN: "))

# if entered_pin == pin:

#     amount = int(input("Withdraw Amount: "))

#     if amount <= balance:
#         balance -= amount
#         print("Withdraw Successful")
#         print("Balance:", balance)

#     else:
#         print("Insufficient Balance")

# else:
#     print("Wrong PIN")

# choice = int(input("Choose: "))

# match choice:

#     case 1:
#         print("Login")

#     case 2:
#         print("Register")

#     case 3:
#         print("Profile")

#     case 4:
#         print("Logout")

#     case _:
#         print("Invalid")


firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

if firstName and lastName:
    print("Name is: " + firstName + " " + lastName)
else:
    print("Please enter both names!")