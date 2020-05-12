print('函数式编程 --- 函数作为返回值')

'''
1. 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
2. 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
   相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
'''
# 立刻求和的函数：
def calc_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print("测试立刻求和的函数：", calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 函数作为返回值
def lazy_sum(*args):
    def sum():
        result = 0
        for i in args:
            result += i
        return result
    return sum
test_sum = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('测试函数作为返回值实现延迟加载：', test_sum())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
'''

'''
闭包
1. 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
   所以，闭包用起来简单，实现起来可不容易
2. 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用时才执行
3. 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
4. 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
   无论该循环变量后续如何更改，已绑定到函数参数的值不变
'''

# 返回函数时引用循环变量导致的bug
print('测试返回函数时引用循环变量导致bug的情形：')
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print("f1 =", f1())
print("f2 =", f2())
print("f3 =", f3())

# 三个函数的结果全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，
# 因此最终结果为9

print("修改上面代码中的bug：")
def count2():
    def f(i):
        def g():
            return i * i
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f4, f5, f6 = count2()
print("f4 =", f4())
print("f5 =", f5())
print("f6 =", f6())


'''
小结:
1. 一个函数可以返回一个计算结果，也可以返回一个函数。
2. 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''