class Monster():

    def __init__(self, name, tax_num, monster_type):
        self.name = name.title()
        self.tax_num = tax_num
        self.monster_type = monster_type.title()

    # def get_tax_num(self):
    #     return self.__tax_num
    #
    # def set_tax_num(self, new_num):
    #     self.__tax_num = new_num
    #     return f'New tax num for {self.name} is {new_num}'
