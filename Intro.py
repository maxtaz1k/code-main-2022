# 12 Digital Technology

score = 0  # declares the score variable
counter = 0  # declare the counter variable

name = input("What is your name?\n")
print("Hello " + name + "!\n")
print("Welcome to my Marine Animals quiz, " + name + " this quiz will teach you about the endangered marine life in our oceans!\n")

def intro():
    print("""Welcome to my quiz about endangered marine animals!""")

intro()

def question(question, choices):  # Function with two parameters
    print(question)  # Prints question
    for question in choices:  # Prints choices
        print(question)

