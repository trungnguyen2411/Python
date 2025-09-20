temperature = float(input("Enter the temperature: "))


def water_state(temperature):
    if 0 < temperature < 100:
        return "Liquid"
    elif temperature <= 0:
        return "Solid"
    else:
        return "Gas"


print(water_state(temperature))


# Solution:
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
