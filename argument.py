def greet(name):
    print(f"Hello {name}")

greet("Araful")


def user(name, age):
    print(name)
    print(age)

user("Araful", 27)

def user(name, age):
    print(name)
    print(age)

user(
    age=27,
    name="Araful"
)


def create_user(
    name,
    role="user"
):
    print(name)
    print(role)

create_user("Araful")

def numbers(*args):
    print(args)

numbers(10, 20, 30)


def create_user(**kwargs):
    print(kwargs)

create_user(
    name="Araful",
    age=27,
    job="Flutter Developer"
)





add =lambda a,b: a+b

print("add",add(5,55))