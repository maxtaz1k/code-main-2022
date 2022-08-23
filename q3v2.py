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
