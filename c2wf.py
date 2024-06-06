def load_content():
    f = open ("students_records.txt") #store the data in f
    f2 = f.readlines() #reads all lines as string
    student_records = [] #creating list
    for line in f2: #reading each line in records
        if len(line) <= 1:
            continue
        line = line.strip() #removes space
        line = line.split() #splits string into list
        line = tuple(line) #converts to tuple
        student_records.append(line) #adds into student records
    return student_records
#open the file in write mode and write the student details
def save_file(student_details,argument):
    argument2 = argument 
    if argument2 == "change file":
        f = open ("students_records.txt", "w+")
        for line in student_details:
            line = " ".join(line)
            line = "\n" + line
            f.writelines(line)
        f.close()
    elif argument2 == "Save data": 
        print("Data has been saved.")#print a message indicating that data has been saved

def add_new_student(): #function to add a new student to the records
    student_records = load_content() #load existing student records
    new_student = []
    name = input("Enter name: ")
    new_student.append(name)
    #get input for name, ID, subject, and mark
    while True:
        ID= input("Enter ID: ")
        IDcheck = (ID.isdigit())
        if IDcheck == False:
            print("Enter number as ID: ")
            continue
        else:
            break
    new_student.append(ID)
    subject = input("Enter subject: ")
    new_student.append(subject)
    while True:
        marks = input("Enter marks(use ',' to seperate if multiple'): ")
        marks = marks.split(",")
        valid_marks = True    
        for mark in marks:
            mark = int(mark)
            if mark > 100 or mark < 0:
                print ("Please enter a valid mark.")
                valid_marks = False
                break
        if valid_marks == True:
            marks = " ".join(marks)
            new_student.append(str(marks))
            break
    #add the new student to the records and save the file
    new_student = tuple(new_student) #convert to tuple
    student_records.append(new_student)
    save_file(student_records, 'change file')

def update_student_info():
    f = load_content()
    student_located = False
    while not student_located:
        askid = input("Enter ID: ") #ask user which student to update through ID
        askcourse = input("Enter course: ")
        for line in f:
            studentID = line[1] #indicating that index 1 is ID
            student_course = line[2] #indicating that index 2 is courses
            if askid == studentID and askcourse == student_course:
                student_index = f.index(line)
                details = list(line)
                student_located = True
        if student_located == False:
            print("Pls enter Valid ID or course: ")
            continue
        if student_located == True:
            append = False
            update = False
            while not update or append:
                askuser = input("Do you wish to update or add a mark? ")
                if askuser == "add":
                    current_student = details[3:] #adds marks after subject column
                    if len(current_student) >= 5: #limiting to a max of 5 marks
                        print ("You can not add any more marks.")
                    else:
                        while True:
                            marks = input("Enter marks: ")
                            marks = marks.split(",")
                            valid_marks = True
                            for mark in marks:
                                mark = int(mark) #converts every mark to integer
                                if mark > 100 or mark < 0:
                                    print ("Please enter a valid mark.")
                                    valid_marks = False
                                    break 
                                    
                            if valid_marks == True:
                                details = list(details)
                                marks = " ".join(marks) #joins wherever there is space
                                details.append(str(marks))
                                details = tuple(details)
                                f[student_index] = details #indexing
                                save_file(f)
                            break
                elif askuser == "update":
                    while True:
                        marks = input("Enter marks: ")
                        marks = marks.split(",") #split on every comma
                        valid_marks = True
                        for mark in marks:
                            mark = int(mark)
                            if mark > 100 or mark < 0: #validity check
                                print ("Please enter a valid mark.")
                                valid_marks = False
                                break
                        if valid_marks == True:
                            marks = " ".join(marks)
                            del details[3:] #deletes all marks
                            details.append(str(marks))
                            details = tuple(details)
                            f[student_index] = details
                            save_file(f, 'change file')
                            break
                break        
            
def delete_student():
    f = load_content()
    student_located = False
    while not student_located:
        askid = input("Enter ID you want to delete: ")
        askcourse = input("Enter course: ")
        for line in f:
            studentID = line[1]
            student_course = line[2]
            if askid == studentID and askcourse == student_course:
                student_index = f.index(line)
                student_located = True
        if student_located == False:
            print("Pls enter Valid ID or course: ")
            continue
        if student_located == True:
            del f[student_index] #deletes full row
            save_file(f, 'change file')
            break
    
def search_student ():
    f = load_content()
    student_located = False
    while not student_located:
        askid = input("Enter ID you want to search: ")
        for line in f:
            studentID = line[1]
            if askid == studentID: #if entered ID is same it will print it out
                print(line)
                student_located = True
        if student_located == False:
            print("Student not found :(")  
    
def sort_student ():
    f = load_content()
    course_input = input("What course do you want to sort? ")
    students_in_course = []
    student_located = False
    for line in f: #selection sort
        student_course = line[2]
        if course_input == student_course:
            students_in_course.append(line)
            student_located = True
    if student_located == False:
        print("There are no students in this course :(")
    else:
        for start in range(len(students_in_course)):
            max_index = start
            for i in range(start+1, len(students_in_course)): 
                if students_in_course[i][1] > students_in_course[max_index][1]:
                    max_index = i
            students_in_course[start], students_in_course[max_index] = students_in_course[max_index], students_in_course[start]
        for line in students_in_course:
            print(line)

def descriptive_stats():
    f = load_content()
    students_in_course = []
    course_found = False
    while True:
        user_input = input("Enter the name of the course for which you want the descriptive stats of the students: ")
        for student in f:
            student_course = student[2]
            if user_input == student_course:
                students_in_course.append(student)
                course_found = True
        if course_found == False:
            print("There are no students in this course, try a different course.")
        else:
            min_mark = 0
            max_mark = 0
            student_name_maximum_score = None
            student_name_minimum_score = None
            failed_students = []
            
            first_mark = True
            for student in students_in_course:
                student_mark = student[3:]
                student_mark = list(student_mark)                    
                student_name=student[0] 
                for mark in student_mark:
                    mark = int(mark)
                    if first_mark:
                        max_mark = mark
                        min_mark = mark
                        student_name_maximum_score = student_name
                        student_name_minimum_score = student_name
                        first_mark = False
                    elif mark > max_mark:
                        student_name_maximum_score = student_name
                        max_mark = mark
                    elif mark < min_mark:
                        student_name_minimum_score = student_name
                        min_mark = mark
                for i in range(0,len(student_mark)):
                    student_mark[i] = int(mark)
                student_final_mark = sum(student_mark)/5
                if student_final_mark < 50:                    
                    student_final_mark = str(student_final_mark)
                    student_final_mark = student_name + " - " + student_final_mark
                    failed_students.append(student_final_mark)
            print("For the following record: ")
            for student in students_in_course:
                print(student)
            print(f"Max Grade: {student_name_maximum_score} - {max_mark} ")
            print(f"Minimum Grade: {student_name_minimum_score} - {min_mark} ")
            
            if len(failed_students) == 0:
                print("No students failed the course.")
            else:
                print("Students who failed the course:")
                for student in failed_students:
                    print(student)
            break
def print_all():
    f = open ("students_records.txt") #store the data in f
    f2 = f.readlines() #reads all lines as string
    student_records = [] #creating list
    for line in f2: #reading each line in records
        if len(line) <= 1:
            continue
        line = line.strip() #removes space
        line = line.split() #splits string into list
        line = tuple(line) #converts to tuple
        print(line) #prints all lines as tuple
        student_records.append(line) #adds into student records
    return student_records
    
def factory_reset(): #open the file in write mode and clear its contents
    f = open("students_records.txt", "w+")
    confirmation = input("Are you sure you want to perform a factory reset? This will delete all student records. (yes/no): ")
    if confirmation.lower() == "yes":
        f.write("")
        print("Factory reset completed. All student records have been deleted.")
    else:
        print("No student records found :(")
    