def get_max():
    grades = [9.5, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return f"Max: {maximum}, Min: {minimum}"


print(get_max())


# Solution:
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message


print(get_max())
