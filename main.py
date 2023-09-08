# Day 30

# # File not found Error
# with open("myfile.txt") as file:
#     file.read()

# try:
#     file = open("myfile.txt")
#     my_dict = {"key": "value"}
#     print(my_dict["fake key"])
# except FileNotFoundError:
#     file = open("myfile.txt", "w")
#     file.write("We made the file for you!")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise IndexError("Woah")
#     # file.close()
#     # print("File was closed")

# # Calling our own errors
# try:
#     ht = float(input("Height: "))
#     wt = int(input("Weight: "))
#
#     if ht > 3:
#         raise ValueError("Height should not be over 3 meters.")
#
# except ValueError as error_msg:
#     print(error_msg)
# else:
#     bmi = wt / ht ** 2
#     print(bmi)

# fruits = ["Apple", "Pear", "Orange"]
#
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(2)

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
# print(total_likes)


# # KeyError
# my_dict = {"key": "value"}
# value = my_dict["keys"]

# # IndexError
# fruit_list = ["apple", "banana", "peach"]
# fruit = fruit_list[3]

# #TypeError
# text = "abc"
# print(text+5)
