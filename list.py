# fruits = ["Apple", "Banana", "Mango"]


# print(fruits)


# print(type(fruits))

# fruits = ["Apple", "Banana", "Mango","C"]

# print(fruits[0])
# print(fruits[2])
# print(fruits[-2])
# print(fruits[-1])
# print(fruits[-3])
# f= fruits[1]="A"
# print(f)


# fruits.append("Pen")

# print(fruits)

# fruits = ["Apple", "Mango"]

# fruits.insert(0, "Banana")

# print(fruits)


# numbers = [1, 2]

# numbers.extend([3, 4])

# print(numbers)

# fruits = ["Apple", "Banana", "Mango"]

# fruits.remove("Banana")

# print(fruits)

fruits =["apple", "banana","mango"]

# removed_item= fruits.pop(1)

# print(removed_item)
# print(fruits)

# # del fruits [1]


# # del fruits[0:2]
# print(fruits)
# fruits.clear()
# print(fruits)

print(len(fruits))


skills =["flutter","java","dart","python"]


name ="python"

if name in skills :
    print(name,"found")
else :
    print(name,"not found")

for i in skills:
    print(i)

for index,i in enumerate (fruits):
    print(index,i)

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

numbers = [50, 10, 30, 20]

# numbers.sort()

# print(numbers,"Sort")

numbers.reverse()
print(numbers,"Reversed")
# numbers = [1, 2, 3, 4]

# numbers.reverse()

# print(numbers)

users = [
    ["Rahim", 25],
    ["Karim", 30],
    ["Araful", 27]
]

print(users[2][0],"age",users[2][1])

users = [
    {
        "name": "Rahim",
        "age": 25
    },
    {
        "name": "Araful",
        "age": 27
    }
]

print(users[1]["name"])

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)

print(even_numbers)

user = ["Araful", 27, "Flutter Developer"]

name, age, job = user

print(name)
print(age)
print(job)

# List Methods Cheat Sheet
# Method	কাজ
# append()	শেষে item add
# insert()	index-এ add
# extend()	multiple item add
# remove()	value remove
# pop()	index remove + return
# clear()	সব remove
# index()	index খোঁজা
# count()	কয়বার আছে
# sort()	sort
# reverse()	reverse
# copy()	copy
