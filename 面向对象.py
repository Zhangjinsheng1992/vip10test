# #创建类
# class washer():
#     def wash(self):
#         print('我会洗衣服')
# #创建对象
# haier1=washer()
# haier1.wash()

# #类外定义属性
# haier1.width=500
# haier1.height=800
# print(f'haier1的宽度是{haier1.width} ')
# print(f'haier1的高度是{haier1.height}')

#类内部定义属性
#创建类
class washer():
    def __init__(self,width,height,brand):
        self.width=width
        self.height=height
        self.brand=brand
    def print_info(self):
        print(f'宽度是{self.width}')
        print(f'高度是{self.height}')
        print(f'品牌是{self.brand}')
    def __str__(self):
        return f'这是{self.brand}洗衣机的说明书'
    def __del__(self):
        print(f'我被删除了')
#创建对象
haier2=washer(300,600,'海尔')
#调用方法

haier2.print_info()
print(haier2)
del haier2
