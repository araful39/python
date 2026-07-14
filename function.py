# print("Hello")
# print("Welcome to Python")
# print("Hello Araful")
# print("Welcome to Python")

# print("Hello Rahim")
# print("Welcome to Python")

# def welcom():
#     print("Hi Python")
# welcom()

# def welcom2(name):
#     print("Welcome to",name)

# welcom2("Dhaka")


# def sum(a, b):
#     print(a+b)

# sum(5,6)

def sum(a, b):
    return a+b

print(sum(5,10))

def total(a, b):
    return a-b

total = total(30,5)

print(total)


def welcom(guest ="guest"):
    print("Hello",guest)

welcom("Araful")
welcom()


def user(name, age):
    print("Your name", name)
    print("Your age ",age)

# user(
#     name="Raju",
#     age=27
# )


# user(

#      age=27,
#     name="Raju",
   
# )


# user(

#      age="Raju",
#     name=27
   
# )


# def add(*numbers):
#     # print(numbers)
#     return list(numbers)

# print(add(10,20,30,40))


def add(*numbsers):
    total =0
    for i in numbsers:
        total += i

    return total

print(add(10,20,30,40))

def calculate(a, b):
    add = a+b
    subtract =a-b

    return add, subtract
result =calculate(20,30)
print(result)


add_result,sub_result = calculate(5,5)

print(add_result)
print(sub_result)



def login(email, password):
    if not email:
        return "Email required"
    if not password:
        return "Password required"
    return "Login Success"

print(login("aa","aa"))




name="Raju"


def createName():
    print(name)



createName()



# def add (a,b):
#     return a +b

add =lambda a, b :a+b
print(add(10,20))

  
def countdown(number):
    if number == 0:
     return 
    print(number)

    countdown(number-1)

countdown(6)


def add(a: int, b: int) -> int:
    return a + b

def add(a: int, b: int) -> int:
    return a + b