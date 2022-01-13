class InvalidInput( Exception ):
    pass

class Gradebook:
    def __init__(self):
        self.gradebook = {}
    def get_name(self):
        name = input('Enter student name: ')
        return name
    def get_grade(self):
        # assume grades will be integers separated by commas and no spaces.
        grade = input('Enter student grade(s): ')
        grade = grade.split(',')
        grade = [int(i) for i in grade]
        return grade
    def set_dict(self, name, grade):
        if len(name) > 0:
            self.gradebook[name] = grade
        else:
            raise InvalidInput
    def add_student(self):
    # Add student: Creates a new entry in a dictionary called `gradebook.` The user will input the key (a student’s name) and the value (a list of grades).
        proceed = True
        while proceed:
            student_name = self.get_name()
            print('A new student! Adding them to the gradebook...')
            student_grade = self.get_grade()
            if student_name in self.gradebook.keys():
                print('Oops, this student already exists in the gradebook.')
                proceed = False
            else:
                self.set_dict(student_name, student_grade)
                proceed = False
    def view_gradebook(self):
        print(self.gradebook)
    def calculate_avg_grade(self):
        name = self.gradebook.keys()
        avg_grades_dict={}
        for student in self.gradebook.keys():
            total_score = 0
            total_tests = 0
            for grade in self.gradebook[student]:
                total_score = total_score + grade
                total_tests += 1
            avg_grade = total_score / total_tests
            avg_grades_dict[student] = avg_grade
        print(avg_grades_dict)
    def quit(self):
        print('End of program')





foo = Gradebook()
foo.add_student()
foo.view_gradebook()
foo.add_student()
foo.view_gradebook()
foo.calculate_avg_grade()


# decision = input('What would you like to do?: ')
# while lower(decision) != 'quit':
#     if lower(decision) == :
#     elif :
#     elif :
#     else:
#         print('Unrecognised operation. Try again.')
#
# if decision == 'add student':
#     add_student()
# if decision == 'view gradebook':
#     view_gradebook()
