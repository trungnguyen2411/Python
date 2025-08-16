file = open("../bear.txt", 'r')
content = file.read()
print(content)

Solution:
file = open("bear.txt")
content = file.read()
print(content)
