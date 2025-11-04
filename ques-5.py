try:
    # get numbers from the user
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    # find max and min
    max_num = max(numbers)
    min_num = min(numbers)

    # save list, max, and min to a file
    with open("minmax_data.txt", "w") as file:
        file.write(f"Numbers: {numbers}\n")
        file.write(f"Maximum: {max_num}\n")
        file.write(f"Minimum: {min_num}\n")

    # read and show the file content
    with open("minmax_data.txt", "r") as file:
        print("File content:\n", file.read())

except ValueError:
    print("Please enter only numbers separated by spaces, like: 10 20 30 40")
