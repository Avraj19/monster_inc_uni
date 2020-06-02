from monster_class import Monster
from student_monster_class import Student_monster
from course_class import Course

# Create two student objects
print('Create two student objects')
sully = Student_monster('Sully', 568, 'Ghost Type', 'st-15', ['Shadow body'])
scar_crow = Student_monster('Scar Crow', 7859, 'Bag face monster', 8845, ['Shadow seth '])
print('\n')

# Add a skill to each of your student
sully.add_skill('enlarging claw')
scar_crow.add_skill('Scream')
print(scar_crow.student_details())
print(sully.student_details())
print('\n')

# Create(initialize) a course
scar_tac = Course('Scar Tactics', '01/06/2020', [])
print(scar_tac.module, scar_crow.name, scar_tac.start_date)
print('\n')

# Append student object / instances to list of student attributes in one of the courses

scar_tac.add_student('scar_crow')
scar_tac.add_student('sully')
print('\n')

# EXTRA - get the list of students, itterate over it and print the students name
print(scar_crow.student_details())
print(sully.student_details())