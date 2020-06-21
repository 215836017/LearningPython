print('学习列表list')

'''
1. list简介 -- 动态数组
1). Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
2). 用索引来访问list中每一个位置的元素，记得索引是从0开始的
3). 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
4). append -- 往list中追加元素到末尾
   insert -- 把元素插入到指定的位置
   pop -- 删除list末尾的元素
   pop(i) -- 删除指定位置(i处)的元素
   要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
5). list里面的元素的数据类型也可以不同, 元素也可以是另一个list
'''
names = []
print('id(names):', id(names))

classmates = ['abc', '123', 'def', '456', 'ghj', '789']
print('classmates is:', classmates)
print('classmates.len =', len(classmates))

print('\n\ntest 1111111: 使用下标')
print('classmates[0] =', classmates[0])
classmates[0] = "修改0"
print('修改后，classmates[0] =', classmates[0])
print('classmates[2] =', classmates[2])
print('classmates[3] =', classmates[3])
print('classmates[-1] =', classmates[-1])
print('classmates[-4] =', classmates[-4])
classmates[-4] = '修改-4'
print('修改后，classmates[-4] =', classmates[-4])

print('\n\ntest 2222222: 使用循环')
for s in classmates:
    print('s = ', s)

print('\n\ntest 33333333333333: append()方法')
classmates.append('app_1')
classmates.append('app_2')
for s in classmates:
    print('s = ', s)


print('\n\ntest 44444: insert()方法')
classmates.insert(0, 'insert_1')
classmates.insert(2, 'insert_2')
for s in classmates:
    print('s = ', s)


print('\n\ntest 5555555: pop()方法')
classmates.pop()
classmates.pop(2)
for s in classmates:
    print('s = ', s)
