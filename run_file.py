from student_monster_class import Student_monster
from course_class import Course

#     def __init__(self, name, tax_num, monster_type, student_num, skill_list):
scar_crow = Student_monster('Scar Crow', 7859, 'Bag face monster', 8845, ['Shadow seth '])

print(scar_crow.student_details())

scar_crow.add_skill('Scream')

print(scar_crow.student_details())

scar_tac = Course('Scar Tactics', [scar_crow], '01/06/2020')

print(scar_tac.module, scar_crow.name, scar_tac.start_date)