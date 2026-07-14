# Set হলো Python-এর একটি collection যা unique (duplicate ছাড়া) value রাখে।


numbers = {10,20, 20, 30, 10}

print(numbers)
print(type(numbers))

items = {"Python","Dart"}
skills = {
    "Python",
    "Flutter",
    "Dart"
}

for skill in skills:
    print(skill)

    skills = {
    "Python",
    "Dart"
}

skills.add("Flutter")

print(skills)

skills = {
    "Python"
}

skills.update(
    ["Flutter","Dart"]
)

print(skills)
skills.remove("Python")

print(skills)
numbers = {10,20,30}

print(len(numbers))
skills = {
    "Python",
    "Flutter"
}


if "Python" in skills:
    print("Found")

    python_students = {
    "Rahim",
    "Karim",
    "Araful"
}


flutter_students = {
    "Araful",
    "Jamal",
    "Sakib"
}

all_students = (
    python_students |
    flutter_students
)

print(all_students)

a = {3}

b = {1,2,3,4}


print(a.issubset(b))



# 25. Set vs List
# Feature	List	Set
# Duplicate	✅ রাখে	❌ রাখে না
# Order	থাকে	থাকে না
# Index	আছে	নেই
# Mutable	Yes	Yes
# Search	Slow	Fast
# Use	Sequence	Unique data


# 26. Set vs Tuple
# Feature	Tuple	Set
# Duplicate	রাখে	রাখে না
# Order	থাকে	থাকে না
# Change	❌	✅
# Index	আছে	নেই

# 27. Set vs Dictionary
# Feature	Set	Dictionary
# Data	Value	Key + Value
# Example	{1,2,3}	{"id":1}
# Key	নেই	আছে
# JSON Object	❌	✅


allowed_ips = {
    "192.168.1.10",
    "192.168.1.20"
}


ip = "192.168.1.10"


if ip in allowed_ips:
    print("Allowed")

#  30. Set কখন ব্যবহার করবো?

# Use Set যখন:

# ✅ Duplicate remove করতে হবে
# ✅ দ্রুত search দরকার
# ✅ Unique permission/data রাখতে হবে
# ✅ Membership check করতে হবে