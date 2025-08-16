1:
file_a = open("../a.txt", "r")
file_a = file_a.read()
print(file_a)

file_b = open("../b.txt", "r")
file_b = file_b.read()
print(file_b)

file_c = open("../c.txt", "r")
file_c = file_c.read()
print(file_c)

2:
filenames = ["a.txt", "b.txt", "c.txt"]

for filename in filenames:
    file = open(f"../{filename}", "r")
    content = file.read()
    print(content)


Solution:
filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)

