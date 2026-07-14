names = ["Rahim", "Karim", "Araful"]

for name in names:
    print(name)

    name = "Python"

for char in name:
    print(char)

for number in range(1, 6):
    print(number)


    skills = [
    "Flutter",
    "Python",
    "Cyber Security"
]

for skill in skills:
    print(skill)

    colors = (
    "Red",
    "Green",
    "Blue"
)

for color in colors:
    print(color)

    permissions = {
    "read",
    "write",
    "delete"
}

for permission in permissions:
    print(permission)

    skills = [
    "Flutter",
    "Python",
    "Security"
]

for index, skill in enumerate(skills):
    print(index+1, skill)


for number in range(1, 10):

    if number == 5:
        break

    print(number)


for number in range(1, 6):

    if number == 3:
        continue

    print(number)


    users = ["Rahim", "Karim", "Araful"]

search_user = "Sakib"

for user in users:

    if user == search_user:
        print("User Found")
        break

else: 
    print("User Not Found")


    correct_password = "1234"

attempt = 0
max_attempts = 3

while attempt < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Success")
        break

    attempt += 1

    remaining = max_attempts - attempt

    print(f"Wrong Password")
    print(f"Remaining Attempts: {remaining}")