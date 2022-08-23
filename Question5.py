#Fith question

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