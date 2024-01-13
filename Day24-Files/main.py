file = open("Day24-Files/myfile.txt")
contents = file.read()
print(contents)
file.close()


with open("Day24-Files/myfile.txt") as file:
    contents = file.read()
    print(contents)