from functions import *

#MAIN PART
if __name__=='__main__':  
    #Hard-coded deadline is December 1, 2021
    date_deadline = [2021, 12, 1, 23, 59]
    print("Deadline for CW submission is 01/12/2021 (December 1, 2021) 23:59!\n")
    student1 = Student_MC(date_deadline)
    student1.main()
