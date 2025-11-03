s = input("Enter numbers separated by spaces: ")
nums = []
for x in s.split():
    nums.append(int(x))

total = 0
for n in nums:
    total += n

avg = total / len(nums)

f = open("numbers_data.txt", "w")
f.write("Numbers: " + str(nums) + "\n")
f.write("Sum: " + str(total) + "\n")
f.write("Average: " + str(avg) + "\n")
f.close()

f = open("numbers_data.txt", "r")
print("\nFile contents:")
print(f.read())
f.close()