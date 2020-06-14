#!/usr/bin/env python3

# 标题: Python中的if-else语句

"""
语句：
    条件判断语句
    循环语句
"""

'''·
1. 条件语句： 
   if else
   *** Python中没有 switch语句 ***
'''

'''
2. 使用if时, 直接使用变量名，则是对变量名进行值判断空或判断0
'''
userName = ""
if userName:
    print('userName is not null')
else:
    print('userName is null...')

if userName != '':
    print('userName is not null')
else:
    print('userName is null...')

a = 1111
if a:
    print('ok ok ok')
else:
    print('no no no')

'''
3. Python中的else if的写法为：elif
'''
num = 9
if num < 10:
    print('1111111111')
elif num >= 10 and num < 20:  # 此处有更简洁的写法： 10 <= num < 20
    print('22222222')
else:
    print('333333333')

'''
4. pass关键字
'''
print('\n\ntest  4444444444')
if (10 < 7):
    pass
else:
    print('hhhhhhhhhhhh')

'''
1. 因为input()返回的类型是str，所以必须先把str转换成整数。Python提供了int()函数来完成这件事情
2. 如果输入abc呢？又会得到一个错误信息, int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了,
此时可以通过捕获运行时错误来处理
 '''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')