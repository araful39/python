users = [
    {
        "name": "Rahim",
        "is_active": False
    },
    {
        "name": "Araful",
        "is_active": True
    }
]

user = users[1]

if user["is_active"]:
    print(f'{user["name"]} is Active')
else:
    print(f'{user["name"]} is Inactive')


url = "https://app.com/payment/success?status=paid"

if "status=paid" in url:
    print("Payment Success")

elif "status=failed" in url:
    print("Payment Failed")

elif "status=pending" in url:
    print("Payment Pending")

else:
    print("Unknown Payment Status")





filename = "report.PDF"

filename = filename.lower()

if filename.endswith(".pdf"):
    print("PDF File")

elif filename.endswith(".jpg"):
    print("Image File")

elif filename.endswith(".py"):
    print("Python File")

else:
    print("Unknown File")

    user = {
    "name": "Araful",
    "role": "admin",
    "is_active": True,
    "is_blocked": False
}

if (
    user.get("is_active")
    and not user.get("is_blocked")
):

    if user.get("role") == "admin":
        print("Full Access")

    elif user.get("role") == "manager":
        print("Manager Access")

    else:
        print("Normal Access")

else:
    print("Access Denied")