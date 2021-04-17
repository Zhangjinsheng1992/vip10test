
# open(test.txt,r)
#
# try:
#     f=open(test.txt,r)
# except:
#     f=open(test.txt,w)
#异常
try:
    print(1)
except Exception as msg:
    print(msg)
else:
    print('我是else，没有异常')
finally:
    print('有没有异常我都执行')