print('函数式编程 --- 装饰器')

'''
1. 由于函数也是一个对象， 而且函数对象可以被赋值给变量，通过变量也能调用该函数
2. 函数对象有一个name属性，可以拿到函数的名字。

'''

def testZSQ():
    print('test ZSQ')

funName1 = testZSQ.__name__
f1 = testZSQ
funName2 = f1.__name__
print("通过__name__属性获取函数的名字：funName1 =", funName1)
print("通过__name__属性获取函数的名字：funName2 =", funName1)

'''
1. 现在，假设我们要增强testZSQ()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
   这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
2. 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator
3. 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
'''
def log(func):
    def wrapper(*args, **kw):     # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
        print('call %s():' %func.__name__)  # 首先打印日志
        return func(*args, **kw)    # 再紧接着调用原始函数
    return wrapper

#因为log是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
@log
def testZSQ2():
    print('test ZSQ2 ')
@log
def testZSQ3():
    print('2018-07-04 20:00 ')


print("测试装饰器：", testZSQ2())
print("测试装饰器：", testZSQ3())



print('如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数:')
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

print("返回decorator的高阶函数: ", now())