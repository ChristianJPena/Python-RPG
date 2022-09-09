# Python RPG

# Learning objective: Use and practice Python fundamentals, with an emphasis on Single Responsibility functions.

# Technologies: Python, Functions, Data Types, Flow Control (Conditionals), Loops, Dictionary/List Data Structures

# Extra Credit Points: 5

# DONE.You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.

# Features:

# As a developer, I want to make at least five commits on GitHub with descriptive messages.

# As a user, I want an engaging story to be told using print() statements.

# As a user, I want Hercules (and each enemy), to have health, attack power, and a List of attack names saved in a Dictionary.

# As a user, I want the ability to select Hercules’ attack using a menu prompt.

# As a user, I want the foe’s attack to be chosen at random.

# As a user, I want the results of each attack to be logged in the terminal.

# As a developer, I want to use an Attack() function that will terminate when Hercules or an enemy’s health reaches zero.

# As a developer, I want my RunGame() function to call my other functions in a logical order that will determine game flow.

# As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!


import random

def welcome_screen ():
    print("\nWelcome to...\nPython \n¡RPG!\n")
    print("You are Hercules, the greatest of the Greek Heroes! \n\nYou have been tasked by 👑King Eurystheus👑 to: \n\nslay the vicious \n🦁Nemean Lion🦁 \n\ndefeat the impossible nine-headed \n🐍Lernaean Hydra🐍 \n\nUltimately, capturing the guard dog of the underworld \n🐕Cerberus🐕\n")
    print("¡Lets begin your quest!\n")
welcome_screen()

full_health = 100
enemy_health = 120
user_punch = 15
user_kick = 20
user_bite = 50




# def Attack():
#     ~


# def RunGame(): #Master Function
#     Attack()
