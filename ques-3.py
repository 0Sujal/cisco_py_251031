# get a sentence from the user
sentence = input("Enter a sentence: ")

# split it into words
words_list = sentence.split()

# make all words uppercase
words_tuple = tuple(w.upper() for w in words_list)

# save both list and tuple in a file
with open("sentence_data.txt", "w") as file:
    file.write(str(words_list) + "\n")
    file.write(str(words_tuple) + "\n")

# read the file and show the content
with open("sentence_data.txt", "r") as file:
    print("File content:\n", file.read())
