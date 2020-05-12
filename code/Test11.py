print('函数式编程 --- 高阶函数 --- 内建函数：map/reduce')

'''
map/reduce
1. map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
2. map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2次方，还可以计算任意复杂的函数
'''
# 比如我们有一个函数f(x)=x2次方，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下
def f(x):
    return x * x

test_map = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print('test map:', list(test_map))

'''
1. reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
   其效果就是：
   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
#比方说对一个序列求和，就可以用reduce实现

from functools import reduce;
def add(x, y):
    return x + y

def chengFa(x, y):
    return x * y
print('test_reduce1: ', reduce(add, [1, 3, 5, 7, 9]))
print('test_reduce2: ', reduce(chengFa, [1, 3, 5, 7, 9]))


print('\n\n 函数式编程 --- 高阶函数 --- 内建函数：filter')
'''
1. Python内建的filter()函数用于过滤序列
2. 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
   然后根据返回值是True还是False决定保留还是丢弃该元素
'''
# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    return n % 2 == 1
print('test_filter: ', list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))




print('\n\n 函数式编程 --- 高阶函数 --- 内建函数：sorted')
'''
1. 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
   但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来
2. Python内置的sorted()函数就可以对list进行排序
3. 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
'''

test_sorted1 = [1, 5, 6, 8, 2, 3, 4, 9, 7]
test_sorted2 = sorted(test_sorted1)
print('before orted: ', test_sorted1)
print('after  orted: ', test_sorted2)

test_sorted3 = [3, 7, -1, -2, 9]
test_sorted4 = sorted(test_sorted3, key=abs)
print('before orted: ', test_sorted3)
print('after  orted: ', test_sorted4)  # 打印结果：after  orted:  [-1, -2, 3, 7, 9]  即按绝对值大小排序

test_sorted5 = ['bob', 'about', 'Zoo', 'Credit']
test_sorted6 = sorted(test_sorted5)   # 默认情况下，对字符串排序，是按照ASCII的大小比较的, 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print('before orted: ', test_sorted5)
print('after  orted: ', test_sorted6)
test_sorted7 = sorted(test_sorted5, key=str.lower)
print('after  orted: ', test_sorted7)
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
test_sorted8 = sorted(test_sorted5, key=str.lower, reverse=True)
print('after  orted: ', test_sorted8)