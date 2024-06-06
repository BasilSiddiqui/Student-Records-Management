#Welcome message
msg1 = '''
============================================
       Heriot-Watt University System 
   Student Records Management Application 
============================================

Welcome, esteemed faculty member!
'''
#Choice of commands message
msg2 = '''
------------------------------------------
1: Add a new student
2: Update student course grade 
3: Delete student
4: Search for a student
5: Sort students by ID 
6: Get descriptive statistics for a course
7: Save student records to file
8: Load student records from file
9: Factory reset 
10: Exit
------------------------------------------
'''
print(msg1)
#Importing all functions
from c2wf import load_content
from c2wf import add_new_student
from c2wf import save_file
from c2wf import update_student_info
from c2wf import delete_student
from c2wf import search_student
from c2wf import sort_student
from c2wf import descriptive_stats
from c2wf import factory_reset
from c2wf import print_all
#Using defined functions according to the user input
while True:
    print (msg2)
    user_input = input("Choose a service from the menu above: ")
    if user_input == "1":
        add_new_student()
    elif user_input == "2":
        update_student_info()
    elif user_input == "3":
        delete_student()
    elif user_input == "4":
        search_student()
    elif user_input == "5":
        sort_student()
    elif user_input == "6":
        descriptive_stats()
    elif user_input == "7":
        save_file(',', 'Save data')
    elif user_input == "8":
        print_all()
    elif user_input == "9":
        factory_reset()
    elif user_input == "10":
        break



 


