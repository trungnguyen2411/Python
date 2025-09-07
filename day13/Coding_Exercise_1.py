year_of_birth = int(input("What is your year of birth? "))


def get_age(year_of_birth, current_year=2025):
    age = current_year - year_of_birth
    return age


print(get_age(year_of_birth, current_year=2025))


# Solution:
def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age
