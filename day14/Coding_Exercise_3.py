temperature = float(input("Enter the temperature: "))


def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    else:
        return "Cold"


print(foo(temperature))


# Solution:
def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"
