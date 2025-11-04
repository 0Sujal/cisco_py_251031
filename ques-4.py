# get names from the user
names = input("Enter names separated by spaces: ").split()

# sort names alphabetically
names.sort()

# convert list to tuple
names_tuple = tuple(names)

# save both in a file
with open("names_data.txt", "w") as file:
    file.write(str(names) + "\n")
    file.write(str(names_tuple) + "\n")

# read and display the file content
with open("names_data.txt", "r") as file:
    print("File content:\n", file.read())
