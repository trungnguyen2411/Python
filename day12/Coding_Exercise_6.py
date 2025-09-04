name = input("What is your name? ")


def get_name(name):
    uppercase_name = name.capitalize()
    return f"Hi {uppercase_name}"


print(get_name(name))


# Solution:
def foo(name):
    return f"Hi {name.title()}"
