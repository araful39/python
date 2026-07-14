# Dart List
# List<String> names = ["Rahim", "Karim"];

# Python List
# names = ["Rahim", "Karim"]

names = ("Rahim", "Karim")


print(names)
print(type(names))

print(len(names))
print(list(names))
print(names[0])
print(names[-1])
# print(names(1))
print(names[1:4])
# names[1]="Raju"
print(names)
skills = (
    "Flutter",
    "Python",
    "Security"
)

if "Python" in skills:
    print("Found")

    numbers = (10,20,20,30)

print(numbers.count(20))

numbers = (10,20,30)

print(numbers.index(20))

data = (
    ("Araful",27),
    ("Rahim",25)
)


print(data[0][0])

numbers = (10,20,30)

new_list = list(numbers)

print(new_list)

numbers = (10,20,30)

new_list = list(numbers)

print(new_list)

numbers = [10,20,30]

new_tuple = tuple(numbers)

print(new_tuple)

a = (1,2,3)
b = (1,2,3)

print(a == b)



# Tuple vs List
# Feature	List	Tuple
# Syntax	[]	()
# Mutable	✅ Yes	❌ No
# Speed	Normal	একটু faster
# Methods	বেশি	কম
# Change	করা যায়	যায় না
# Use	Dynamic data	Fixed data