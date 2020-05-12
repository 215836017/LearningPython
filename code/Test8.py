print("函数")

'''
1. 可以直接从Python的官方网站查看内建函数的文档  https://docs.python.org/3/library/index.html
2. 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且给出错误信息
3. 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息
4. Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
5. 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
   然后，在缩进块中编写函数体，函数的返回值用return语句返回
'''


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(3))
print(my_abs(-4))

'''
1. 如果想定义一个什么事也不做的空函数，可以用pass语句
2. pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
3. pass还可以用在其他语句里，比如：

if age >= 18:
    pass
缺少了pass，代码运行就会有语法错误
4. 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
   但是如果参数类型不对，Python解释器就无法帮我们检查
5. 数据类型检查可以用内置函数isinstance()实现， 比如对参数类型做检查，只允许整数和浮点数类型的参数。
'''


def nop():
    pass


def my_abs2(x):
    if not isinstance(x, (int, float)):
        #  raise TypeError('bad operand type')    # 错误和异常处理将在后续学习
        #  print('bad operand type')
        return 'bad operand type'
    if x >= 0:
        return x
    else:
        return -x


print(my_abs2('abc'))

'''
1. 函数可以返回多个值吗？答案是肯定的
2. 但其实这只是一种假象，Python函数返回的仍然是单一值, 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
   而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
'''


def my_test():
    return 'abc', 123, 'def', 456, 0.33


print('返回多个值：', my_test())

'''
位置参数
1. 除了正常定义的必选参数(位置参数)外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，
   还可以简化调用者的代码
2. 以计算平方的函数为例：
    def power(x):
        return x * x
    如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数
    可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
    def power(x, n):
       s = 1
       while n > 0:
           n = n - 1
           s = s * x
       return s
'''
print('测试位置参数：')


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s  # 这里 只写了return竟然也返回了s，好神奇！


print("test power:", pow(3, 2))
print('test power:', pow(3, 5))
'''
默认参数:
1. 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用
2. 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
   这样，当我们调用power(5)时，相当于调用power(5, 2), 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)
3. 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
   一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
   二是如何设置默认参数。
   当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
4. 定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
print('测试默认参数：')


def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print('test power2:', power2(3))
print('test power2:', power2(3, 5))
'''
可变参数
1. 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
2. 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
3. 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])

这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
>>> nums = [1, 2, 3]
>>> calc(*nums)
'''
print('测试可变参数：')


def calcs(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print("test calcs:", calcs(1, 2, 3, 4))
print("test calcs:", calcs(1, 2, 3, 4, 5))
print("test calcs:", calcs(1, 2, 3, 4, 5, 6))
nums = [1, 2, 3]
print('test calcs:', calcs(*nums))
'''
关键字参数
1. 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名
   的参数，这些关键字参数在函数内部自动组装为一个dict
2. 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
   但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
   其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求
3. 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
4. **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
   注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
'''
print('测试关键字参数：')


def person(name, age, **kw):
    print('name :', name, "，age :", age, "，other :", kw)


person('Person1', 10)
person('Person2', 20, city='杭州')
person('Person3', 30, city='beijing', job='Android')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Person4', 40, city=extra['city'], job=extra['job'])
person('Person5', 50, **extra)
'''
命名关键字参数
1. 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
2. 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
3. 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
4. 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
5. 命名关键字参数可以有缺省值，从而简化调用
6. 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
   如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
'''
print('测试命名关键字参数')
def person1(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name :', name, "，age :", age, "，other :", kw)

person1('Person1', 10)
person1('Person2', 20, city='杭州')
person1('Person3', 30, city='beijing', job='Android')
person1('Person3', 30, city='beijing', job='Android', sex='男')

print('用命名关键字参数定义限制关键字参数的函数：')
def person2(name, age, *, city, job):
    print('定义限制关键字参数的函数:', name, age, city, job)

#person2('Person1', 10)                 # 不运行
#person2('Person2', 20, city='杭州')    # 不运行
person2('Person3', 30, city='beijing', job='Android')
#person2('Person3', 30, city='beijing', job='Android', sex='男')   # 报错了

print('如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了')
def person3(name, age, *args, city, job):
    print('person3:', name, age, args, city, job)

person3('Person3_1', 30, city='beijing', job='Android')
person3('Person3_2', 30, 'abc', city='beijing', job='Android')
person3('Person3_3', 30, 'abc', 123, city='beijing', job='Android')

print('命名关键字参数可以有缺省值，从而简化调用')
def person4(name, age, *, city='hangzhou', job):
    print('person4:', name, age, city, job)
person4('Person4_1', 30, job='Android')
person4('Person4_2', 30, city='beijing', job='Android')


'''
参数组合
1. 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
   但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
2. 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
3. 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差

'''
print('测试参数组合')
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args1 = (1, 2, 3, 4)
kw1 = {'d': 99, 'x': '#'}
f1(*args1, **kw1)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


'''
小结
1. 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
2. 要注意定义可变参数和关键字参数的语法：
   *args是可变参数，args接收的是一个tuple；
   **kw是关键字参数，kw接收的是一个dict
'''


'''
1. 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
2. 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
   栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
3. 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的
4. 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
   使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
5. 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
6. 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把fact(n)函数改成尾递归方式，也会导致栈溢出
'''

def fact(num):
    return fact_item(num, 1)

def fact_item(num, product):
    print('product = ', product)
    if num == 1:
        return product

    print('num-1 =', num-1)
    return fact_item(num-1, num * product)

print("测试尾递归：", fact(5))