# try:
#     number = 10/0
# except:
#     print("Something went wrong")


# try:
#     number=10/0
# except ZeroDivisionError:
#      print("Cannot divide by zero")



# try: 
#     age =int(input("Enter your age: "))
# except ValueError:
#     print("Please enter a number")


# try:
#     number = int(
#         input("Enter number: ")
#     )

#     result = 100 / number

#     print(result)

# except ValueError:
#     print("Invalid Number")

# except ZeroDivisionError:
#     print("Zero is not allowed")


# try:
#     number = int(
#         input("Enter number: ")
#     )

#     result = 100 / number

# except (
#     ValueError,
#     ZeroDivisionError
# ):
#     print("Invalid Input")

# try:
#     number = 10 / 0

# except ZeroDivisionError as error:
#     print(error)

try:
    result = 10 / 0

except Exception as e:
    print(
        f"Error: {e}"
    )
try:
    number = int(
        input("Enter number: ")
    )

except ValueError:
    print("Invalid Number")

else:
    print(
        f"Valid Number: {number}"
    )