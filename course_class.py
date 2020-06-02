
class Course():

    def __init__(self, module_name,start_date, student_list=[]):
        self.module = module_name
        self.students = student_list
        self.start_date = start_date

    def add_student(self, new_student):
        self.students.append(new_student)
        return new_student + 'has been added'


    def course_detals(self):
        couse_detals = {
            'Course name': self.module,
            'Start date': self.start_date,
            'Student list': self.students
        }

        for list in couse_detals:
            print(list, ': ', couse_detals[list])

        return ''
