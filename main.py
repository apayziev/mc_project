
""" This program gives information about  Mitigating Circumstances 
to students of Westminster International University """


from functions import isOnTime, within24_hours, submitted_within_5days
# from functions import *
# - this a also applicable way to import functions from module

while True:
    print('------------------------------*****-------------------------------------')
    print("___Welcome to Mitigating Circumsatances (MC) Program___\n"
              "<-- CW Deadline -->\n"
              "<-- CW Submission -->")
    user_input =str(input("Please type 'start' to begin\n"
                              "If you want to quit please type 'quit'\n>>> ")).lower()
    if user_input == 'start':
                isOnTime()
    elif user_input == 'quit':
                break
    else:
                print("\nYou response is incorrect. Type again!!!")




