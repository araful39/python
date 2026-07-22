# # name =input("Enter your name: ")

# # print("Your name is :",name )



# # age=18

# # voterAge= int(input("Enter you age: "))


# # if voterAge >= age :
# #     print("Yor age voter")
# # else:
# #     print("Your are not voters")



# # userName ="admin"
# # password =123456


# # user=input("Enter role: ")
# # password2 =int(input("Enter your password: "))


# # if userName ==user:
# #     if password == password2:
# #         print("Login successfully")
# #     else:
# #         print("invalide creadential")
# # else:
# #         print("Invalide creadential")


# # day =int(input("Enter your number: "))

# # match day:
# #     case 1:
# #         print("A")

# #     case 2:
# #         print("B")

# #     case 3:
# #         print("C")
# #     case 4:
# #         print("D")
# #     case _:
# #         print("Invalide")



# # age =30

# # # if age >= 20:
# # #     print("A")
# # # else :
# # #     print("B")



# # print("Adult") if age >=18 else print("Child")


# # number = 12

# # result = "Even" if number % 2 == 0 else "Odd"

# # print(result)


# # age =int(input("Enter your age: "))

# # if age >=18:
# #     print("Your adult")
# # elif age <=0:
# #     print("Enter valid age")

# # else :
# #     print("Your child")

# # fruits = ["apple", "banana", "cherry"]
# # x, y, z = fruits
# # print(x)
# # print(y)
# # print(z)
# # print(z)


# # user ={
# #     "name":"Araful",
# #     "age":18
# # }

# # print(user["name"])

# # try:
# #     print(10 / 0)
# # except:
# #     print("Error")
# #     file = open("test.txt", "w")
# # file.write("Hello")

# # import math
# # print(math.sqrt(25))


# # a =10
# # b =5
# # c =15.0

# # d=-5

# # print(type(d))
# # print(type(c))

# # a = 10.0
# # b = 5.5

# # result = a + b

# # print(result)

# # number =3+5j
# # number =5

# # print(number)
# # print(type(number))


# # name ="""
# # Hello
# # I am Araful
# # I am learning python

# # """


# # print(name)
# # print(type(name))

# # name = "Python"

# # # for i in name.count:
# # #     print(name[i])

# # numbers = {1, 2, 3, 3, 4}

# # print(numbers)

# # data = b"Hello"

# # print(data)
# # print(type(data))

# # data = bytearray([65, 66, 67])

# # print(data)

# # data = bytearray(b"Python")

# # view = memoryview(data)

# # print(view[0])

# # data = None
# # print("None : ",data)


# # age ="27"
# # print(age)
# # print(type(age))

# # print(type(int(age)))
# # print("---------------------")
# # print(type(float(age)))


# # number =[1,2,3,4,5,6,7,5,6,8,9,]

# # numbers= set(number)

# # print(list(number))

# # fruits = ["Apple", "Banana", "Mango"]

# # for index, fruit in enumerate(fruits, start=1):
# #     print(index ,fruit)


# # if "Apple" in fruits: 
# #         print("Apple Not Found")


# # numbers = [50, 10, 40, 20]

# # numbers.sort()

# # print(numbers)


# # numbers = [1, 2, 2, 2, 3]

# # print(numbers.count(2))




# numbers =[]


# for i in range (1,6):
#  numbers.append(i)
#  print(numbers)
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6]

# even_numbers = [
#     number
#     for number in numbers
#     if number % 2 == 0
# ]

# print(even_numbers)


# fruits = {"Apple", "Banana"}

# fruits.add("Mango")

# fruits.add("Apple")
# fruits.update(("Apple", "Orange"))
# fruits.update(("Mango", "Orange"))
# fruits.update({"Mango", "Orange"})

# fruits.discard("Orange")
# print(fruits)


# name ="araful"

# if "a" in name:
#     print("Yes")
# else:
#     print("No")


# class User:
#     def __init__(self, name, id):
#         print("User create by raju",name,id)

#     @staticmethod
#     def add(a,b):
#         print(a+b)

# user= User("Raju",955)


# user.add(10,20)



# # বাইরের ফাংশন (ক্লাসের বাইরে)
# def external_tax_calc(amount):
#     return amount * 0.05

# class Product:
#     tax_rate = 0.10  # ক্লাস ভেরিয়েবল

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#         # ১. স্ট্যাটিক মেথড কল (self ছাড়া)
#         self.discounted_price = Product._apply_discount(price)

#         # ২. ক্লাস মেথড কল (self ছাড়া)
#         self.tax = Product._get_tax(price)

#         # ৩. বাইরের ফাংশন কল (self ছাড়া)
#         self.final_price = self.discounted_price + external_tax_calc(self.discounted_price)

#     @staticmethod
#     def _apply_discount(price):
#         # এখানে self বা cls নেই
#         return price * 0.90  # ১০% ডিসকাউন্ট

#     @classmethod
#     def _get_tax(cls, price):
#         # এখানে self নেই, শুধু cls আছে (ক্লাস ডেটা অ্যাক্সেসের জন্য)
#         return price * cls.tax_rate

# # অবজেক্ট তৈরি
# p = Product("Laptop", 1000)
# print(p.discounted_price)  # 900.0
# print(p.tax)               # 90.0
# print(p.final_price)       # 900 + 45 = 945.0



