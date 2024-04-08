'''
This program allows a user to register students for an exam venue
'''
# opening the file using 'with'
with open('reg_form.txt', 'w') as file:
    # get user input of how many students to be registered
    n = int(input('Please enter the number of student taking an exam: '))
    
    # ask the user to input the students id, repeat n times
    for i in range(n):
        student_id = input('Please enter the students ID: ')
        # write the student ID to the file
        file.write(student_id + '\t.................\n')