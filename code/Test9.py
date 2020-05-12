print('高级特性')

'''
在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高
'''

print('\n高级特性 --- 切片')

'''
切片
1. 对于经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
2. L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
3. 如果第一个索引是0，还可以省略
4. 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片, 记住倒数第一个元素的索引是-1
5. 甚至什么都不写，只写[:]就可以原样复制一个list
6. tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
7. 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('学习切片1：', L[0 : 3])
print('学习切片2：', L[: 3])
print('学习切片3：', L[-2: ])
L1 = list(range(100))
print('学习切片4，取出前20个数中的偶数', L1[: 20 : 2])
print('学习切片5，所有数，每5个取一个', L1[: : 5])
print('学习切片6，字符串切片：', 'ABCDEFG'[:3])


print('\n高级特性 --- 迭代')
'''
迭代
1. 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
2. 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的
3. Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。list这种数据类型虽然有下标，
   但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
4. 由于字符串也是可迭代对象，因此，也可以作用于for循环
5. 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
6. 如果要对list实现类似Java那样的下标循环怎么办？
   Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
'''
print('学习迭代1：')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, ':', d[key])

print('学习迭代2：')
for value in d.values():
    print(value)

print('学习迭代3：')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print('学习迭代4：')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


print('\n高级特性 --- 列表生成式')
'''
列表生成式
1. 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
2. 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11)),
   但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
   方法一是循环,但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
3. 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
4. for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
5. 还可以使用两层循环，可以生成全排列
6. 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
7. 列表生成式也可以使用两个变量来生成list
8. 小结: 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁
'''
test_compre1 = [x * x for x in range(1, 11)]
print('学习列表生成式1： ', test_compre1)
test_compre2 = [x * x for x in range(1, 11) if x % 2 == 0]
print('学习列表生成式2： ', test_compre2)
test_compre3 = [m + n for m in 'abc' for n in 'xyz']
print('学习列表生成式3： ', test_compre3)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
test_compre4 = [k + '=' + v for k, v in d.items()]
print('学习列表生成式4： ', test_compre4)


print('\n高级特性 --- 生成器')
'''
生成器
1. 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
   不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可以按照
   某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
   在Python中，这种一边循环一边计算的机制，称为生成器：generator
2. 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator  
3. 我们怎么打印出generator的每一个元素呢？如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值 
4. generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
5. 不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象, 并且不需要关心StopIteration的错误
6. 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
7. 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
   而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''
test_list1 = [x * x for x in range(10)]
test_generator1 = (x * x for x in range(10))
print('学习生成器1：', test_list1)
print('学习生成器2：', test_generator1)

print('\n高级特性 --- 迭代器')
'''
1. 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
   一类是集合数据类型，如list、tuple、dict、set、str等；
   一类是generator，包括生成器和带yield的generator function。
   这些可以直接作用于for循环的对象统称为      可迭代对象：Iterable。
   可以使用isinstance()判断一个对象是否是Iterable对象
2. 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。 
   可以被next()函数调用并不断返回下一个值的对象称为      迭代器：Iterator。
   可以使用isinstance()判断一个对象是否是Iterator对象
3. 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
4. 为什么list、dict、str等数据类型不是Iterator？
   这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出
   StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算
   下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
5. Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的
'''