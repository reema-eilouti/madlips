import re

# 1. file with Text \n
# 2. open file .py \n
# 3. read el txt File
# 4. find where the spaces are
# 5. figure out the spaces types
# 6. prompt the user to fill in 
# 7. write on the file
# 8. view the final file to user


filename = "madlips.txt"

my_file = open(filename, "r")

my_file2 = my_file.read()

reg_ex = r"\(.*?\)"

words = re.findall(reg_ex, my_file2)

user_words = []

for word in words:
    user_word = input(f"Please insert a word as {word} : ")
    user_words.append(user_word)

# print(user_words)



# with open(new_file, "r+") as f:
#     readable_file = f.read()
#     readable_file = re.sub(reg_ex, *user_words, readable_file)
#     f.seek(0)
#     f.write(readable_file)
#     f.truncate()

new_text = re.sub(reg_ex, user_words[0], my_file2, count = 1)

for i in range(1,len(words)):
    new_text = re.sub(reg_ex,user_words[i],words[i], count = 1)



with open("new_madlip.txt", 'w') as f:
    f.write(new_text)



# print(new_text)
# print(words)

# test_list = []

# for i in range(len(words)):
#     test_list.append(f"{words[i]}, {user_words[i]}")


# print(test_list)