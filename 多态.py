# class Dog():
#     def work(self):
#         print('指哪打哪。。。')
# class Armydog(Dog):
#     def work(self):
#         print('追赶敌人')
# class Drugdog(Dog):
#     def work(self):
#         print('追查毒品')
# class Person():
#     def work_with_dog(self,dog):
#         dog.work()
#
# ad=Armydog()
# dd=Drugdog()
# daqiu=Person()
# daqiu.work_with_dog(ad)
# daqiu.work_with_dog(dd)

#类属性
# class Dog():
#     tooth=10
# wangcai=Dog()
# xiaohei=Dog()
# print(wangcai.tooth)
# print(xiaohei.tooth)
# #修改类属性
# Dog.tooth=20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)
# #修改实例属性
# wangcai.tooth=15
# print(wangcai.tooth)
# print(xiaohei.tooth)
#类方法
# class Dog():
#     __tooth=10
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
# xiaobai=Dog()
# result=xiaobai.get_tooth()
# print(result)
#静态方法

class Dog():
    @staticmethod
    def info_print():
        print('这是一个狗类的静态方法')
xiaohua=Dog()
xiaohua.info_print()
Dog.info_print()

