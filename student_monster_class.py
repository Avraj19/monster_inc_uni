from monster_class import Monster


class Student_monster(Monster):

    def __init__(self, name, tax_num, monster_type, student_num, skill_list=[]):
        super().__init__(name, tax_num, monster_type)
        self.student_num = student_num
        self.skill_list = skill_list

    def add_skill(self, new_skill):
        self.skill_list.append(new_skill)
        return

    def student_details(self):
        details = {
            'Name': self.name,
            'Tax_num': self.tax_num,
            'monster_type': self.monster_type,
            'student_num': self.student_num,
            'skill_list': self.skill_list
        }

        for list in details:
            print(list, ': ', details[list])
        return ''
