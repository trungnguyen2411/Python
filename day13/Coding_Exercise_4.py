x = int(input("Enter the temperature: "))


def temperature(x):
    if x > 7:
        return "Warm"
    else:
        return "Cold"


print(temperature(x))


# Solution:
def foo(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
