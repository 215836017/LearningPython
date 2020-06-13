#!/usr/bin/env python3

# 标题: Python中的布尔值

"""
1. 一个布尔值只有True、False两种值，要么是True，要么是False
2. 在Python中，可以直接用True、False表示布尔值（请注意大小写）,也可以通过布尔运算计算出来
3. 布尔值可以用and、or和not运算。
"""
print('3 > 2 =', 3 > 2)
print('3 > 5 = ', 3 > 5)
print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and False = ", False and False)
print("5 > 3 and 3 > 1 = ", (5 > 3 and 3 > 1))

print("True or True = ", True or True)
print("True or False = ", True or False)
print("False or False = ", False or False)
print("5 > 3 or 1 > 3 = ", 5 > 3 or 1 > 3)
print("not True = ", not True)
print("not False = ", not False)
print("not 1 > 2 = ", not 1 > 2)

'''
2. 布尔值经常用在条件判断中
'''
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

'''
3. is 也是一个关系运算符
'''
age1 = 20
print('age: ', id(age))
print('age1: ', id(age1))
print('age is age1', age is age1)

a = 10
b = 100000000
print('a: ', id(a))
print('b: ', id(b))
print('a is b', a is b)

a = 100000000
print('----------------')
print('a: ', id(a))
print('b: ', id(b))
print('a is b', a is b)

# TODO：在交互式环境中有个坑： 即Python中的小整数对象池和大整数对象池
'''
在小于等于数值256时：a和b的数值相同时，a is b的结果为True
在大于数值256时：a和b的数值相同时，a is b的结果为False
'''

'''
1. 在Python中也有三目运算符，格式如下：
   真结果 if 表达式 else 假结果
'''
n1 = 6
n2 = 7
result1 = n1 + n2 if n1 > n2 else n2 - n1
result2 = n1 + n2 if n1 < n2 else n2 - n1
print('result1 = ', result1)
print('result2 = ', result2)

