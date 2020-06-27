print('通用的序列操作 -- 内置函数')

'''
1. 使用内置函数获取序列的长度
'''
name = ['aaa', 'bbb', 123, 0.99, "hello"]
print('name.len = ', len(name))
'''
打印结果：
name.len =  5
'''

'''
2. 使用内置函数获取序列中最大、最小值
'''
# print('max(name) = ', max(name)) # TypeError: '>' not supported between instances of 'int' and 'str'
# print('min(name) = ', min(name)) # TypeError: '<' not supported between instances of 'int' and 'str'

number = [0.99, 100, 30, 0.001, 4000, 3]
print('max(number) = ', max(number))
print('min(number) = ', min(number))
'''
打印结果：
max(number) =  4000
min(number) =  0.001
'''
