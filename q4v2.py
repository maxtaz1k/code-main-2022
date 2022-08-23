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
