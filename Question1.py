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
