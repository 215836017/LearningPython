print('使用list和tuple')

'''
标题：使用list和tuple
'''

'''
list
1. Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
2. 用索引来访问list中每一个位置的元素，记得索引是从0开始的
3. 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
4. append -- 往list中追加元素到末尾
   insert -- 把元素插入到指定的位置
   pop -- 删除list末尾的元素
   pop(i) -- 删除指定位置(i处)的元素
   要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
5. list里面的元素的数据类型也可以不同, 元素也可以是另一个list
'''
classmates = ['abc', '123', 'def', '456', 'ghj', '789']
print('classmates is:', classmates)


'''
tuple
1. 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改, 它也没有append()，insert()这样的方法。
其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
2. 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
3. 如果要定义一个空的tuple，可以写成()
4. 但是，要定义一个只有1个元素的tuple，如果你这么定义: test_tuple222 = (1) ,定义的不是tuple，是1这个数！这是因为括号()
既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
'''
classmates_tuple = ('abc', '123', 'def', '456', 'ghj', '789')    # tuple 和 list 写法上的区别：方括号和圆括号。
print('classmates_tuple is:', classmates_tuple)
test_tuple111 = ()
print('test_tuple111 is:', test_tuple111)
test_tuple222 = (1)
test_tuple333 = (1,)
test_tuple444 = ('a')
print('test_tuple222 is:', test_tuple222)
print('test_tuple333 is:', test_tuple333)
print('test_tuple444 is:', test_tuple444)


'''
“可变的”tuple
1.  test_tuple555 = ('a', 'b', ['A', 'B']), 元组中的元素不会和不能改变，但是list中的元素却是可以变化的，导致元组看起来变化了。
'''
test_tuple555 = ('a', 'b', ['A', 'B'])
print('test_tuple555 is:', test_tuple555)
test_tuple555[2][0] = 'x'
test_tuple555[2][1] = 'Y'
print('test_tuple555 is:', test_tuple555)
