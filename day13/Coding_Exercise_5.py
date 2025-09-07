x = input("Enter a password: ")


def password(x):
    if len(x) >= 8:
        return True
    else:
        return False


print(password(x))


# Solution:
def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False
