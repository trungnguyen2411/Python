file = open("../essay.txt", 'r')
content = file.read()
file.close()
content = content.title()
print(content)

# Solution:
file = open("essay.txt", 'r')
content = file.read()
print(content.title())
