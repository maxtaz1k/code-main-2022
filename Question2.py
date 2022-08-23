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
