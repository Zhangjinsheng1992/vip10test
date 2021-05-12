# 单继承
# class Teacher():
#     def __init__(self):
#         self.mifang='五香煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class Student(Teacher):
#     pass
#
# xiaoming=Student()
# print(xiaoming.mifang)
# xiaoming.do()
#多继承
# class Teacher():
#     def __init__(self):
#         self.mifang='五香煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class School():
#     def __init__(self):
#         self.mifang='香辣煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class Student(Teacher,School):
#     pass
#
# xiaoming=Student()
# print(xiaoming.mifang)
# xiaoming.do()

#
# class Teacher():
#     def __init__(self):
#         self.mifang='五香煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class School():
#     def __init__(self):
#         self.mifang='香辣煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class Student(Teacher,School):
#     def __init__(self):
#         self.mifang='独创秘方'
#     def do(self):
#         self.__init__()
#         print(f'使用{self.mifang}制作煎饼')
#     def teacher_do(self):
#         Teacher.__init__(self)
#         Teacher.do(self)
#     def school_do(self):
#         School.__init__(self)
#         School.do(self)
# class Tusun(Student):
#     pass
# xiaoming=Tusun()
# xiaoming.do()
# xiaoming.teacher_do()
# xiaoming.school_do()


# class Teacher():
#     def __init__(self):
#         self.mifang='五香煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
# class School(Teacher):
#     def __init__(self):
#         self.mifang='香辣煎饼'
#     def do(self):
#         print(f'使用{self.mifang}制作煎饼')
#     def old_do(self):
#         super(School,self).__init__()
#         super(School, self).do()
#     def old_do(self):
#         super.__init__()
#         super.old_do()
# class Tudi(School):
#     def


class Master():
    def __init__(self):
        self.kongfu='五香煎饼配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class School():
    def __init__(self):
        self.kongfu='黑马煎饼果子配方'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class Prentice(School,Master):
    def __init__(self):
        self.kongfu='独创煎饼果子配方'
        self.__money=20000
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)
    def get_money(self):
        return self.__money
    def set_money(self,much):
        self.__money=much
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
class Tusun(Prentice):
    pass
xiaoming=Prentice()
print(xiaoming.get_money())
xiaoming.set_money(10000)
print(xiaoming.get_money())
