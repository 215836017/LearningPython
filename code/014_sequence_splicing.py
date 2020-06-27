print('通用的序列操作 -- 序列相加')

letter = ['abc', 'def', 'hij']
letter2 = ['abc', 'def', 'hij']
num = [10, 20, 30, 40]
num2 = [11, 21, 31, 41]

print('num + letter = ', num + letter)
print('num + num2 = ', num + num2)
print('letter + num = ', letter + num)
print('letter + letter2 = ', letter + letter2)
'''
打印结果：
num + letter =  [10, 20, 30, 40, 'abc', 'def', 'hij']
num + num2 =  [10, 20, 30, 40, 11, 21, 31, 41]
letter + num =  ['abc', 'def', 'hij', 10, 20, 30, 40]
letter + letter2 =  ['abc', 'def', 'hij', 'abc', 'def', 'hij']
'''
# print('num + hello = ', num + 'Hello world') # TypeError: can only concatenate list (not "str") to list
# 从报错可知：不能拼接列表和字符串,虽然它们都是序列。一般而言，不能拼接不同类型的序列

