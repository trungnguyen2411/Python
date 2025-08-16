file = open("../essay.txt", 'r')
content = file.read()
print("The number of characters contained in the file:", len(content))


Solution:
file = open("essay.txt", 'r')
content = file.read()

nr_chars = len(content)
print(nr_chars)
