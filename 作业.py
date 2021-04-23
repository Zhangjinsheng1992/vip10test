
# # 1、打印小猫爱吃鱼，小猫要喝水
# #创建类
class Cats():
    #创建方法
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫要喝水')
#创建对象
cat1=Cats()
#调用方法
cat1.eat()
cat1.drink()

#
# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
#创建类
class Person():
    #属性
    def __init__(self,name,weight):
        self.name = name
        self.weight=weight
    def __str__(self):
        return f'{self.name}的体重是{self.weight}公斤'
    #方法
    def do(self):
        print(f'{self.name}爱跑步，爱吃东西')
    def run(self):
        self.weight -= 0.5
        print(f'每次跑步后的体重是{self.weight}公斤')
    def eat(self):
        self.weight += 1
        print(f'每次吃东西后的体重是{self.weight}公斤')
#创建对象
person1=Person('小明',75.0)
#调用方法
person1.do()
person1.run()
person1.eat()
print(person1)
#创建对象
person2=Person('小美',45.0)
print(person2)
#

#
# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
#创建家具类
class Funiture():
    def __init__(self,name,area):
        #家具名字
        self.name=name
        #家具占地面积
        self.area=area
#创建房子类
class Home():
    def __init__(self,address,area):
        #地址
        self.address=address
        #房子面积
        self.area=area
        #房子剩余面积
        self.free_area=area
        self.fueniture=[]
    def __str__(self):
        return f'房子的位置在{self.address},房子的面积是{self.area},房子的家具有{self.fueniture}'
    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.fueniture.append(item.name)
            self.free_area-=item.area
        else:
            print('家具太大，剩余面积不足，装不下')
bed=Funiture('床',4)
chest=Funiture('衣柜',2)
table=Funiture('餐桌',1.5)
home1=Home('北京',50)
home1.add_furniture(bed)
home1.add_furniture(chest)
home1.add_furniture(table)
print(home1)
#
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
#创建类
class Gun():
    def __init__(self,model,bullet_count):
        self.model=model
        self.bullet_count=bullet_count
    def __str__(self):
        return f'{self.model}有{self.bullet_count}颗子弹'
    def shoot(self):
        if self.bullet_count==0:
            print('没有子弹')
            return False
        else:
            self.bullet_count-=1
            print('正在射击')
            return True
    def add_bullet(self,count):
        self.bullet_count+=count
        return f'装了{count}颗子弹'
class Soldeir():
    def __init__(self,name,gun):
        self.name=name
        self.gun=gun
    def __str__(self):
        return f'{self.name}有一把{self.gun}'
    def fire(self):
        if self.gun==None:
            return False
        else:
            self.gun.add_bullet(2)
            self.gun.shoot()
            return True
A=Gun('ak47',3)
B=Soldeir('瑞恩','ak47')
B.gun=A
B.fire()
print(B)
#
# 5.github新建一个仓库，练习克隆，提交，创建分支，切换分支等