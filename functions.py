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
    