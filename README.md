# Student Records Management System

## Overview
This program is a simple Student Records Management System that allows users to store, modify, search, and analyze student data. The system stores student details, including their name, ID, subjects, and marks, in a text file (`students_records.txt`).

## Features
- **Load Student Records**: Reads student data from `students_records.txt`.
- **Save Student Records**: Writes student data back to the file.
- **Add New Student**: Adds a new student record with name, ID, subject, and marks.
- **Update Student Information**: Updates or adds marks for an existing student.
- **Delete Student**: Removes a student record from the file.
- **Search Student**: Searches for a student by ID.
- **Sort Students**: Sorts students in a course based on their ID.
- **Descriptive Statistics**: Provides analysis such as highest and lowest marks, failed students, and average scores for a course.
- **Print All Records**: Displays all student records.
- **Factory Reset**: Deletes all student records from the file.

## How to Use
1. Run the program in a Python environment.
2. Choose an operation from the available functions.
3. Follow the prompts to input data or retrieve information.
4. The program will automatically update `students_records.txt` as needed.

## File Structure
- `students_records.txt`: Stores student records as space-separated values.
- `load_content()`: Reads and loads the file into a list of tuples.
- `save_file(student_details, argument)`: Saves or updates the file based on user input.
- `add_new_student()`: Adds a new student record.
- `update_student_info()`: Updates an existing student’s marks.
- `delete_student()`: Deletes a student’s record.
- `search_student()`: Searches for a student by ID.
- `sort_student()`: Sorts students in a course by their ID.
- `descriptive_stats()`: Provides statistical analysis of student marks.
- `print_all()`: Prints all records.
- `factory_reset()`: Clears all data in the file.

## Notes
- Marks should be between 0 and 100.
- Maximum of 5 marks per student.
- Students are identified by their ID and subject.

## License
This project is free to use and modify for educational purposes.
