print('学习列表list')

'''
1. list简介 -- 动态数组， 即列表是可以修改的
1). Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
2). 用索引来访问list中每一个位置的元素，记得索引是从0开始的
3). 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
4). list里面的元素的数据类型也可以不同, 元素也可以是另一个list
'''
names = []
print('id(names):', id(names))

classmates = ['abc', '123', 'def', '456', 'ghj', '789']
print('classmates is:', classmates)
print('classmates.len =', len(classmates))
print('\n\ntest 1111111111: 使用循环遍历')
for s in classmates:
    print('s = ', s)

numbers = [10, 20, 30]
classmates[0] = numbers
print('\n\ntest 222222222： 列表中包含列表')
for s in classmates:
    print('s = ', s)
'''
2. 空列表：是使用不包含任何内容的两个方括号表示的。
   None： 在Python中，None表示什么都没有。
因此，如果要创建一个可包含10个元素的列表，但是没有任何有用的内容时，可以像如下方式操作：
'''
print('\n\ntest 333333333333: 初始化长度为10的列表')
sequence_10 = [None] * 10
print('sequence_10 = ', sequence_10)
'''
打印结果为：
sequence_10 =  [None, None, None, None, None, None, None, None, None, None]
'''
