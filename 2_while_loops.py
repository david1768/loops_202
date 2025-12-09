
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.
# name = input("enter your name: ")

i = 0
while i < len(colors) and colors[i] != "yellow":
    print(colors[i])
    i += 1

name = input("enter your name: ")







#2
# while name == " ":
#     print("you did not enter your name")
#     name = input(" enter your name: ")
# print(f"Hello {name}")


#1 
# age = int(input("enter your age: "))

# while age < 0:
#     print("age cant be negative")
#     age = int(input ("enter youe age: "))

# print(f"you are {age} years old")


#3

# food = input("enter a food you like (q to quit): ")

# # while not food == "q":
# #     print(f"you like {food}")
# #     food = input("enter another food  you like (q to quit): ")

# # print("bye")

# num = int(input("Enter a # between 1 -10: "))
# while num < 1 or num > 10:
# print(f"{num} is not valid")
# num = int(input("Enter a # between 1 -10: "))
# print (f"Your number is {num}")
