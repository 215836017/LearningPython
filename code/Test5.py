print("条件判断")

'''
标题：条件判断
'''


age = 20

if age >= 18:
    print('age > 18  001')
    print('age > 18  002')
    print('age > 18  003')
    print('age > 18  004')
else:
    print("age !> 18 001")
    print("age !> 18 002")
    print("age !> 18 003")
    print("age !> 18 004")

if age < 10:
    print('age < 10')
elif age < 18:
    print('age > 10 and age < 18')
else:
    print('age > 18')


x = 10
y = 11
if x==10 and y==11:
    print('x=10, y=11')
else:
    print('hehehehe...')

'''
1. 因为input()返回的类型是str，所以必须先把str转换成整数。Python提供了int()函数来完成这件事情
2. 如果输入abc呢？又会得到一个错误信息, int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了, 此时可以通过捕获运行时错误来处理
 '''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')