"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # prints out the location of the head office
    def show_head_office(self):
        print('The head office location is Cape Town')


# creating a subclass of Course
class OOPCourse(Course):
    # initialising subclass
    def __init__(self):
        self.descripstion = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    # prints out details of the course
    def trainer_details(self):
        print(f'This course is about {self.descripstion}, and the led by {self.trainer}.')

    # prints out course ID
    def show_course_id(self):
        print('The course ID is #12345')

# object creation of subclass OOPCourse and method calls
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()