numbers = [10, 20, 30, 40]


def get_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


print(get_average(numbers))


# Solution:
def foo(mylist):
    return sum(mylist) / len(mylist)
