# a = 10
# b = 5
# print(a + b)

# # Operator	কাজ	Example
# # +	যোগ	10 + 5
# # -	বিয়োগ	10 - 5
# # *	গুণ	10 * 5
# # /	ভাগ	10 / 5
# # //	Floor Division	10 // 3
# # %	Remainder	10 % 3
# # **	Power	2 ** 3

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# number =10

# if number %2 == 0:
#     print("Even")
# else:
#     print("Odd")


# x =10

# x += 5

# print(x)

# a = 10
# b = 5

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

age =28

has_id =False

if age >=18 and has_id ==False:
    print("Access Granted")

    role = "admin"

if role == "admin" or role == "manager":
    print("Dashboard Access")

    is_blocked = False

if not is_blocked:
    print("User Allowed")

    username = "admin"
password = "1234"
is_blocked = False

if (
    username == "admin"
    and password == "1234"
    and not is_blocked
):
    print("Login Success")
else:
    print("Login Failed")
url = "https://app.com/payment/success?status=paid"

if "success" in url and "status=paid" in url:
    print("Payment Success")

elif "failed" in url:
    print("Payment Failed")

else:
    print("Payment Pending")

#     Arithmetic
# + - * / // % **

# Assignment
# = += -= *= /= %= **=

# Comparison
# == != > < >= <=

# Logical
# and or not

# Membership
# in
# not in

# Identity
# is
# is not

# Bitwise
# & | ^ ~ << >>