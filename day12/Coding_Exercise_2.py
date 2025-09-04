password = input("Enter the password: ")


def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper_case"] = uppercase

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit
    return result


print(strength(password))
print(strength(password).values())

if all(strength(password).values()):
    print("Strong Password")
else:
    print("Weak Password")


# Solution:
def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"
