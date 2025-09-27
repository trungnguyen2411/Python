fluid_ounce = input("Enter fluid_ounce: ")


def foo(fluid_ounce):
    milliliters = float(fluid_ounce) * 29.57353
    return milliliters


print(foo(fluid_ounce))


# Solution:
def foo(oz):
    return oz * 29.57353
