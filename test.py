# name =input("Enter your name: ")

# print("Your name is :",name )



# age=18

# voterAge= int(input("Enter you age: "))


# if voterAge >= age :
#     print("Yor age voter")
# else:
#     print("Your are not voters")



# userName ="admin"
# password =123456


# user=input("Enter role: ")
# password2 =int(input("Enter your password: "))


# if userName ==user:
#     if password == password2:
#         print("Login successfully")
#     else:
#         print("invalide creadential")
# else:
#         print("Invalide creadential")


# day =int(input("Enter your number: "))

# match day:
#     case 1:
#         print("A")

#     case 2:
#         print("B")

#     case 3:
#         print("C")
#     case 4:
#         print("D")
#     case _:
#         print("Invalide")



# age =30

# # if age >= 20:
# #     print("A")
# # else :
# #     print("B")



# print("Adult") if age >=18 else print("Child")


# number = 12

# result = "Even" if number % 2 == 0 else "Odd"

# print(result)


# age =int(input("Enter your age: "))

# if age >=18:
#     print("Your adult")
# elif age <=0:
#     print("Enter valid age")

# else :
#     print("Your child")

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)
# print(z)


user ={
    "name":"Araful",
    "age":18
}

print(user["name"])

try:
    print(10 / 0)
except:
    print("Error")
    file = open("test.txt", "w")
file.write("Hello")

import math
print(math.sqrt(25))