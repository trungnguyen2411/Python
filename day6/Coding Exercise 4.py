snail = "A snail is a slow-moving mollusk from the class Gastropoda, found on land, in freshwater, and in saltwater."
filename = "file.txt"
file = open(f"../{filename}", "w")
file.write(snail)
file.close()


Solution:
with open("file.txt", "w") as file:
    file.write("snail")
