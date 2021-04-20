#一个老师的类，老师的姓名和性别，教的课程，可以教学，实现：xx老师，性别是xx，教xx课
class Teachers():
    def __init__(self,name,sex,object):
        self.name=name
        self.sex=sex
        self.object=object
    def do (self):
        print(f'{self.name}老师，性别是{self.sex},教{self.object}课')
teacher1=Teachers('黎明','男','语文')
teacher1.do()
#将⼩于房⼦剩余⾯积的家具摆放到房⼦中
#房子类
class Home()：
    #属性：
    def __init__(self,address,area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        #剩余面积
        self.free_area=area
        # 家具列表
        self.furniture = []

    # 房间位置
    def __del__(self):
        return f'房子位于{self.address},占地面积是{self.area},剩余面积是{self.free_area},家具有{self.furniture}'

    #房子方法
    def add_furniture(self,item):

        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print(f'家具太大，装不下')
#家具类：
class Furniture ():
    #属性
    def __init__(self,name,area):
        # 名称
        self.name=name
        # 占地面积
        self.area=area


