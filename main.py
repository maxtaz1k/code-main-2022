# Saving Goal Calculator Program v1
'''I am going to make a program that calculates number of weeks needed to save a particular user inputted amount....'''
# Above are the two style of comments



def display_saving_goal(saving_goal):
    print("I inputted", saving goal)

saving_goal= input ("please enter your saving goal amount")
display_saving_goal(saving_goal)


    def get_weekly_income():
        type_of_income = ""
        while type_of_income not in ["hourly" , "annual"]:
            type_of_income = validate_text_input(
                """do you have hourly wage or annual salary? Please input 'hourly' or 'annual' . """, ["hourly" , "annual"])
        if type_of_income == "hourly":
            while True
                try:
                    hours_per_week = float(input("how many hours do you work per week?"))
                    if hours_per_week>0:
                        break
                except ValueError:
                    print("input a number")
                    while True:
                        try:
                            hourly_wage = float(input("waht is your hourly wage?"))
                            if hourly_wage>0:
                                break
                        except ValueError:
                            print("input a number")
                    weekly_income = hourly_wage * hours_per_week
                    print("weekly income =" , weekly_income)
        elif type_of_income == "annual":
            annual_salary = validate_float("what is your annual salary?")
            if annual_salary>0:
                weekly_income =annual_salary /52
            else:
                pass
    return weekly_income





