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


# First Question

while counter < 3:
    question("Q1. How much rubbish gets dumped into the ocean per year?",
             ["A. 1 Million Metric Tons ", "B. 4 Million Metric Tons", "C. 2 Million Metric Tons", "D. 8 Million Metric Tons"])  # answers for function to call

    answer = input().lower()  # requests answer in lowercase

    if answer == "d":  # If statement to declare correct SHORT answer.
        print('Good job, That is right!')  # Tells the ser they are right
        score = score + 1  # adds 1 to score
        counter = 4  # sets counter to 4 - More than 3 - skips to next question

    elif answer == "8 million metric tons":  # If statement to declare LONG answer
        print('Good job, That is right!')  # tells the user they are right through the elif answer
        score = score + 1  # adds 1 to overall score
        counter = 4  # sets counter to 4 and skips to the next question
        break  # break the loop - if correct
    else:  # Else - All other answers
        print('Sorry that is wrong, try again')  # Tells user that they are wrong
        counter = counter + 1  # Adds one to the counter

print("your score is", score)  # Tells user their score
print('\n')  # prints a space for next question

counter = 0

# second Question

while counter < 3:
    question("Q2. What is the largest marine animal?",
             ["A. Gold fish", "B. Blue whale", "C. Great white shark", "D. Sperm Whale"])  # answers for function to call

    answer = input().lower()  # requests answer in lowercase

    if answer == "b":  # If statement to declare corect SHORT answer.
        print('Nice work! The Blue Whale can reach up to 30m long and 200 tons, the blue whale is aslo endangered with only 15,000 still alive!!')  # Tells the user they are right
        score = score + 1  # adds 1 to score
        counter = 4  # sets counter to 4 - More than 3 - skips to next question

    elif answer == "blue whale":  # If statement to declare LONG answer
        print(
            'Nice work! The Blue Whale can reach up to 30m long and 200 tons, the blue whale is aslo endangered with only 15,000 still alive!!')  # tells the user they are right through the elif answer
        score = score + 1  # adds 1 to overall score
        counter = 4  # sets counter to 4 and skips to the next question
        break  # break the loop - if correct
    else:  # Else - All other answers
        print('Sorry that is wrong, try again')  # Tells user that they are wrong
        counter = counter + 1  # Adds one to the counter

print("your score is", score)  # Tells user their score
print('\n')  # prints a space for next question

counter = 0

# Third Question

while counter < 3:
    question("Q3. Which shark species only has a population of 3,500?",
             ["A. Mako Shark", "B. Goblin Shark", "C. Whale Shark", "D. Great White Shark", ])  # answers for function to call

    answer = input().lower()  # requests answer in lowercase

    if answer == "d":  # If statement to declare corect SHORT answer.
        print('Amazing! The Great White shark known to be the deadliest shark is an endangered species!')  # Tells the ser they are right
        score = score + 1  # adds 1 to score
        counter = 4  # sets counter to 4 - More than 3 - skips to next question

    elif answer == "great white shark":  # If statement to declare LONG answer
        print(
            'Amazing! The Great White shark known to be the deadliest shark is an endangered species!')  # tells the user they are right through the elif answer
        score = score + 1  # adds 1 to overall score
        counter = 4  # sets counter to 4 and skips to the next question
        break  # break the loop - if correct
    else:  # Else - All other answers
        print('Sorry that is wrong, the correct answer was d')  # Tells user that they are wrong
        counter = counter + 1  # Adds one to the counter

print("your score is", score)  # Tells user their score
print('\n')  # prints a space for next question

counter = 0

# Fourth question

while counter < 3:
    question("Q4. How many turtles die per year from pollution in the oceans?",
             ["A. 230 ", "B. 500 ", "C. Over 1000", "D. 900 ", ])  # answers for function to call

    answer = input().lower()  # requests answer in lowercase

    if answer == "c":  # If statement to declare corect SHORT answer.
        print('Correct! Over 1000 sea turtles are estimated to die per year due to pollution!')  # Tells the ser they are right
        score = score + 1  # adds 1 to score
        counter = 4  # sets counter to 4 - More than 3 - skips to next question

    elif answer == "over 1000":  # If statement to declare LONG answer
        print('Correct! Over 1000 sea turtles are estimated to die per year due to pollution!')  # tells the user they are right through the elif answer
        score = score + 1  # adds 1 to overall score
        counter = 4  # sets counter to 4 and skips to the next question
        break  # break the loop - if correct
    else:  # Else - All other answers
        print('Sorry that is wrong, the correct answer was C')  # Tells user that they are wrong
        counter = counter + 1  # Adds one to the counter

print("your score is", score)  # Tells user their score
print('\n')  # prints a space for next question

counter = 0

# Fith question

while counter < 3:
    question("Q5. How many different endangered marine species are there?",
             ["A. 237", "B. 473", "C. 1219", "123", "E. 4500 ",
              "F. 2270"])  # answers for function to call

    answer = input().lower()  # requests answer in lowercase

    if answer == "f":  # If statement to declare corect SHORT answer.
        print('yessir! There are 2270 endangered marine animals in our oceans')  # Tells the ser they are right
        score = score + 1  # adds 1 to score
        counter = 4  # sets counter to 4 - More than 3 - skips to next question

    elif answer == "2270":  # If statement to declare LONG answer
        print('yessir! There are 2270 endangered marine animals in our oceans')  # tells the user they are right through the elif answer
        score = score + 1  # adds 1 to overall score
        counter = 4  # sets counter to 4 and skips to the next question
        break  # break the loop - if correct
    else:  # Else - All other answers
        print('Sorry that is wrong, the correct answer was F')  # Tells user that they are wrong
        counter = counter + 1  # Adds one to the counter

print("your score is", score)  # Tells user their score
print('\n')  # prints a space for next question

counter = 0

