print("函数式编程 --- 匿名函数")

'''
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。在Python中，对匿名函数提供了有限支持
'''

# 举个栗子
test_unNameFun = list(map(lambda x : x*x , [1, 2, 3, 4, 5, 6, 7, 8]))
print('测试匿名函数：')
print("test_unNameFun:", test_unNameFun)

'''
1. 通过结果可以看出， 匿名函数lambda x: x * x实际上就是：
   def f(x):
      return x * x
2. lambda 表示匿名函数，冒号前面的x表示函数的参数
3. 匿名表达式有个限制：只能有一个表达式，不用写return， 返回值就是该表达式的结果
4. 匿名函数有个好处：因为函数没有名字，不必担心函数名冲突。
5. 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用函数。
6. 同样， 也可以把匿名函数作为返回值进行返回。
'''

f = lambda x : x * x + 3

print("测试匿名函数赋值给变量：", f(5))
print("测试匿名函数赋值给变量：", f(6))


def build(x, y):
    return lambda : x * x + y * y

print("测试匿名函数作为返回值：")

test_unNameFun1 = build(2, 3)
test_unNameFun2 = build(4, 5)
print('test_unNameFun1 =', test_unNameFun1())
print('test_unNameFun2 =', test_unNameFun2())