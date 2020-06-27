print('列表中的方法：')
'''
1. 在列表中，内建的方法有很多，可以直接使用  object.method(arg) 的方式来调用列表的方法
'''

classmates = ['abc', '123', 'def', '456', 'ghj', '789']
'''
2. append -- 往list中追加元素到末尾
'''
print('\n\ntest 222222: append()方法')
classmates.append('app_1')
classmates.append('app_2')
for s in classmates:
    print('s = ', s)

'''
3. insert -- 把元素插入到指定的位置
'''
print('\n\ntest 33333333: insert()方法')
classmates.insert(0, 'insert_1')
classmates.insert(2, 'insert_2')
for s in classmates:
    print('s = ', s)

'''
4. pop -- 删除list末尾的元素,并返回这个元素
   pop(i) -- 删除指定位置(i处)的元素
   pop是唯一既修改列表又返回一个非None值的列表方法
'''
print('\n\ntest 4444444444: pop()方法')
classmates.pop()
classmates.pop(2)
for s in classmates:
    print('s = ', s)

'''
5. clear -- 就地清空列表中的内容
'''
print('\n\ntest 55555555555555: clear')
list5 = [1, 2, 3]
print('before clear, list5 = ', list5)
list5.clear()
print('after clear, list5 = ', list5)
'''
打印结果：
before clear, list5 =  [1, 2, 3]
after clear, list5 =  []

作用和使用切片赋值：list5[:] = [] 效果相同
'''

'''
6. copy -- 复制列表
'''
print('\n\ntest 6666666666: copy')
list6 = [1, 2, 3, 4, 5, 6]
list6_1 = list6
print('copy 1111111')
print('list6 = ', list6)
print('list6_1 = ', list6_1)
print('copy 222222')
list6[0] = 10
list6_1[1] = 20
print('list6 = ', list6)
print('list6_1 = ', list6_1)
'''
打印结果：
copy 1111111
list6 =  [1, 2, 3, 4, 5, 6]
list6_1 =  [1, 2, 3, 4, 5, 6]
copy 222222
list6 =  [10, 20, 3, 4, 5, 6]
list6_1 =  [10, 20, 3, 4, 5, 6
'''
'''
要让list6 和 list6_1 指向不同的列表，就必须将list6_1 关联到list6的副本
'''
print('copy 333333')
list6_2 = list6.copy()
list6[3] = 30
list6_2[4] = 40
print('list6 = ', list6)
print('list6_2 = ', list6_2)
'''
打印结果：
copy 333333
list6 =  [10, 20, 3, 30, 5, 6]
list6_2 =  [10, 20, 3, 4, 40, 6]
'''

'''
7. count -- 计算指定的元素在列表中出现了多少次
'''
print('\n\ntest 77777777: count')
list7 = list('HelloPython')
count1 = list7.count('o')
print('count1 = ', count1)
'''
打印结果：
count1 =  2
'''

'''
8. extend -- 能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提供给extend，也就是
   说，可以使用一个列表来扩展另一个列表
'''
list8_1 = [1, 2, 3, 4]
list8_2 = [11, 22, 33, 44]
print('\n\ntest 88888888: extend')
print('user + , result = ', list8_1 + list8_2)
print('after user + , list8_1 = ', list8_1)
print('after user + , list8_2 = ', list8_2)
list8_1.extend(list8_2)
print('after extend, list8_1 = ', list8_1)
'''
打印结果：
user + , result =  [1, 2, 3, 4, 11, 22, 33, 44]
after user + , list8_1 =  [1, 2, 3, 4]
after user + , list8_2 =  [11, 22, 33, 44]
after extend, list8_1 =  [1, 2, 3, 4, 11, 22, 33, 44]
'''
'''
总结： 1：拼接(+) 是使用副本进行操作的，不会修改原来的列表
      2：extend是在对象列表的基础上进行操作。
'''

'''
9. index -- 在列表中查找指定值第一次出现的索引
'''
print('\n\ntest 999999999: index')
list9 = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni', 'who']
index1 = list9.index('who')
# index2 = list9.index('w')  #元素不存在时会报错：ValueError: 'w' is not in list
print('index1 = ', index1)
'''
打印结果：
index1 =  4
'''

'''
10. remove -- 删除第一个指定值的元素
'''
print('\n\ntest 10 10 10: remove')
list10 = ['to', 'be', 'or', 'not', 'to', 'be']
list10.remove('be')
print('after remove, list10 = ', list10)
'''
打印结果：
after remove, list10 =  ['to', 'or', 'not', 'to', 'be']
'''

'''
11. reverse -- 对列表进行倒序, 在列表自身的基础上修改，不返回新的列表
'''
print('\n\ntest 11 11 11: reverse')
list11 = [1, 2, 3, 4, 5, 6]
print('before reverse, list11 = ', list11)
list11.reverse()
print('after reverse, list11 = ', list11)
'''
打印结果：
before reverse, list11 =  [1, 2, 3, 4, 5, 6]
after reverse, list11 =  [6, 5, 4, 3, 2, 1]
'''

'''
12. sort -- 用于对列表进行就地排序，即对原列表进行修改
'''
print('\n\ntest 12 12 12 12: sort')
list12 = [3, 5, 7, 9, 2, 4, 6, 8]
list12.sort()
print('after sort, list12 = ', list12)
list12_1 = list('Python')
list12_1.sort()
print('after sort, list12_1 = ', list12_1)
'''
打印结果：
after sort, list12 =  [2, 3, 4, 5, 6, 7, 8, 9]
after sort, list12_1 =  ['P', 'h', 'n', 'o', 't', 'y']
'''

'''
13. sort高级排序 
'''
print('\n\ntest 13 13 13 13: sort')
list13_1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
list13_1.sort(reverse=True)
print('after sort, list13_1 = ', list13_1)
list13_2 = [1, 22, 333, 444]
# list13_2.sort(key=len) # 报错：TypeError: object of type 'int' has no len()
list13_3 = ["22", "333", "1", "444"]
list13_3.sort(key=len)
print('after sort, list13_3 = ', list13_3)
'''
打印结果：
after sort, list13_1 =  [9, 8, 7, 6, 5, 4, 3, 2, 1]
after sort, list13_3 =  ['1', '22', '333', '444']
'''
