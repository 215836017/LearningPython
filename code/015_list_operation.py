print("基本的列表操作")

'''
1. 列表是一种序列，所以可以对列表进行所有的标准序列操作：
   索引、切片、拼接和相乘
'''

'''
2. 索引：
   1) 修改列表
   2) 删除元素
'''
classmates = ['abc', '123', 'def', '456', 'ghj', '789']
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

print('\n\ntest 2222222222: del()方法')
del classmates[0]
del classmates[-2]
for s in classmates:
    print('s = ', s)

'''
3. 切片：
   1) 获取元素
   2) 给切片赋值
'''
print('\n\ntest 3333333333, 使用切片')
name = list('Python')
print('name = ', name)
print('name[2:] = ', name[2:])
name[2:] = ['Java', 'C++']
print('after replace: name = ', name)
'''
打印结果：
name =  ['P', 'y', 't', 'h', 'o', 'n']
name[2:] =  ['t', 'h', 'o', 'n']
after replace: name =  ['P', 'y', 'Java', 'C++']
'''

'''
4. 使用切片还可以在不替换原有元素的情况下插入新元素
'''
print('\n\ntest 444444444444')
name1 = list('Hello Python')
name1[1:1] = [2, 3, 4]
print('name1 = ', name1)
'''
打印结果：
name1 =  ['H', 2, 3, 4, 'e', 'l', 'l', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']
'''
