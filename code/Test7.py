print('使用dict和set')

'''
标题：使用dict和set
'''

'''
dict
1. Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
2. list 用中括号， tuple用小括号， dict用大括号
3. 如果key不存在，dict就会报错,要避免key不存在的错误，有两种办法，一是通过in判断key是否存在,
   二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
4. 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
5. 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的
6. 需要牢记的第一条就是dict的key必须是不可变对象
'''
test_dict111 = {'str1': 95, 'str2': 75, 'str3': 'abcdefg', 'str4': '123456'}
print("test_dict111 is:", test_dict111)
print('test_dict111[str1] :', test_dict111["str1"])
print('test_dict111[str3] :', test_dict111["str3"])

print('str5' in test_dict111)

print(test_dict111.get('str5'))
print(test_dict111.get('str5', 'no result'))

test_dict111.pop('str2')
print('after pop, test_dict111 is:', test_dict111)



'''
set
1. set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
2. list 用中括号， tuple用小括号， dict用大括号, set用小括号+中括号+关键字set
2. 要创建一个set，需要提供一个list作为输入集合
3. 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
4. 通过remove(key)方法可以删除元素
5. set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
6. set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错
'''
test_set111 = set([1, 2, 3, 3, 4, 5, 3, 6, 4, 8])
print('test_set111 is: ', test_set111)
test_set111.add(3)
test_set111.add(0)
test_set111.add(9)
print('after add, test_set111 is: ', test_set111)
test_set111.remove(6)
#test_set111.remove(6)  # 不存在报错
test_set111.remove(2)
print('after remove, test_set111 is: ', test_set111)

test_set222 = set([1, 3, 5, 7])
# 交集
result1 = test_set111 & test_set222
# 并集
result2 = test_set111 | test_set222
print('交集：', result1)
print('并集：', result2)