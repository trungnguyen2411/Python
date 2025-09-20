temperature = float(input("Enter the temperature: "))
FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    elif temperature <= FREEZING_POINT:
        return "Solid"
    else:
        return "Gas"


print(water_state(temperature))

# Solution:
FREEZING_POINT = 0
BOILING_POINT = 100


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
