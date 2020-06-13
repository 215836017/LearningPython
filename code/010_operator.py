#!/usr/bin/env python3

# 标题: Python中的运算符

"""
运算符：
    赋值运算符
    算术运算符
    关系运算符
    逻辑运算符
    位运算符
"""

'''
1. 变量重新赋值后，变量的地址会改变
'''
name = 'zhangSan'
name1 = name
print('name: address = ', id(name), '  name = ' + name)
print('name1: address = ', id(name1), ' name1 = ' + name)

print('重新给name赋值')
name = 'liSi'
print('name: address = ', id(name), '  name = ' + name)
print('name1: address = ', id(name1), ' name1 = ' + name)


'''
1. 位运算： 主要是进制之间的转换
'''