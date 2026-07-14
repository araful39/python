# user ={
#     "name":"araful",
#     "age":27,

# }


# print(user)
# print(user["name"])
# print(user["age"])

# print(user.keys())
# print(type(user))
# user["city"] = "Dhaka"
# print(user)
# print(user.get('name'))
# user.pop("age")
# print(user)

# for key in user:
#     print(key)

#     print(len(user))

#     users = [
#     {
#         "id":1,
#         "name":"Rahim"
#     },
#     {
#         "id":2,
#         "name":"Araful"
#     }
# ]


# print(users[1]["name"])
# user = {
#     "name":"Araful",
#     "age":27
# }


# user.update({
#     "age":28,
#     "city":"Dhaka"
# })


# print(user)


numbers = {}

for x in range(5):
    numbers[x] = x*x

print(numbers)

user = {
    "name":"Araful"
}

user.setdefault("age",27)

print(user)




# Dictionary vs List
# Feature	List	Dictionary
# Data	Ordered values	Key-value
# Access	Index	Key
# Example	[10,20]	{"age":27}
# JSON	Array	Object
# Dart	List	Map
# Dictionary Cheat Sheet
# user = {}

# user["name"] = "Araful"

# user.get("name")

# user.keys()

# user.values()

# user.items()

# user.update()

# user.pop()

# user.clear()

# user.copy()



