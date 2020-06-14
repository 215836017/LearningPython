#!/usr/bin/env python3

# 标题: Python中的语句

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
