name = input("Add a new menber: ") + "\n"
file = open("../members.txt", "r")
names = file.readlines()
file.close()

names.append(name)

file = open("../members.txt", "w")
names = file.writelines(names)
file.close()

# Solution:
member = input("Add a new member: ")

file = open("members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open("members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()
