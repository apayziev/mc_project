#This page covers MC progtam functions and whole program devided into three functions


#MC chart program questions assigned in tuple data type and named as mc_questions
mc_questions = (
                'Did you upload it on time?',
                'Was it within 24 hours?',
                'Is there a valid reason?',
                'Did you submitted within 5 days?',
                'Was it accepted?')

#A list data type was used to answer the questions and assigned to mc_answers
mc_answers = ['You will get Full Mark',
              'Minus 10 marks from overall mark but not below 40',
              'Anfortunately, you will get Mark = 0',
              'Deferral reassessment',
              'Late Submission',  'MC']


def isOnTime():
    """This function asks user wheather he/she uploaded it on time or not"""
    
    user_input = str(input(f"{mc_questions[0]}\n>>>")).lower()
    if user_input == 'yes':
        print(f"\n{mc_answers[0]}\n")
    elif user_input == 'no':
        within24_hours()
    else:
        print("You response is incorrect. Type again!!!")
        isOnTime()
    
def within24_hours():
    """This function does next step if isOnTime() function == no """
    
    user_input = str(input(f"{mc_questions[1]}\n>>>")).lower()
    if user_input == 'yes':
        print(f"\n---> {mc_answers[4]}")
        user_input = str(input(f"{mc_questions[2]}\n>>>")).lower()
        if user_input == 'yes':
            print(f"\n---> {mc_answers[-1]}")
            user_input = str(input(f"{mc_questions[-1]}\n>>>")).lower()
            if user_input == 'yes':
                print(f"\n{mc_answers[0]}\n")
            elif user_input == 'no':
                print(f"\n{mc_answers[1]}\n")
            else:
                print("Your response is incorrect. Type again!!!")
                within24_hours()
        elif user_input == 'no':
            print(f"\n{mc_answers[1]}\n")
        else:
            print("You response is incorrect. Type again!!!")
            within24_hours()
    elif user_input == 'no':
        submitted_within_5days()
    else:
        print("You response is incorrect. Type again!!!")
        within24_hours()
        
def submitted_within_5days():
    """This function asks the user CW submitted within 5 days or not
    and performs the remaining operations """
    
    user_input = str(input(f"{mc_questions[3]}\n>>>")).lower()
    if user_input == 'yes':
        user_input = str(input(f"{mc_questions[2]}\n>>>")).lower()
        if user_input == 'yes':
            print(f"\n---> {mc_answers[-1]} (late submission option)")
            user_input = str(input(f"{mc_questions[-1]}\n>>>")).lower()
            if user_input =='yes':
                print(f"\n{mc_answers[0]}\n")
            elif user_input =='no':
                print(f"\n{mc_answers[2]}")
            else:
                print("You response is incorrect. Type again!!!")
                submitted_within_5days()
        elif user_input == 'no':
            print(f"\n{mc_answers[2]}\n")
        else:
            print("You response is incorrect. Type again!!!")
            submitted_within_5days()
    elif user_input == 'no':
        user_input = str(input(f"{mc_questions[2]}\n>>>")).lower()
        if user_input == 'yes':
            print(f"\n-->{mc_answers[-1]} (non-submission/deferall before specified deadline)"
                  f"\n--> Accepted \n-->{mc_answers[3]}\n")
        elif user_input == 'no':
            print(f"\n{mc_answers[2]}\n")
        else:
            print("You response is incorrect. Type again!!!")
            submitted_within_5days()
    else:
        print("You response is incorrect. Type again!!!")
        submitted_within_5days()

