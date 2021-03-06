print('变量的命名和使用')

# 标题：变量的命名和使用
'''
在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
'''

'''
变量在程序中就是用一个变量名表示的，变量名必须是大小写英文、数字和_的组合，且不能用数字开头，比如：
a = 1
变量a是一个整数。

t_007 = 'T007'
变量t_007是一个字符串。

Answer = True
变量Answer是一个布尔值True
'''

'''
查看Python中的关键字时：导入keyword模块后，print(keyword.kwlist)即可
'''

'''
在编程中，在遵守命名规则的基础上，命名变量名时应该做到见名知意。
在Python中，定义变量或方法时推荐使用下划线式定义， 定义类名时推荐使用驼峰式
'''

'''
1. 像Python这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。也就是说：Python是弱类型语言
2. 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言
3. 和静态语言相比，动态语言更灵活
'''
money = 9.9
print("money 111 = ", money, type(money))
money = "9.9元"
print("money 222 = ", money, type(money))
money = '9.9元'
print("money 333 = ", money, type(money))
money = 9
print("money 444 = ", money, type(money))
money = 9.99
print("money 555 = ", money, type(money))

'''
1. 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
2. 在Python中，通常用全部大写的变量名表示常量：例如：
PI = 3.14159265359
但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变
3. 所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
'''

'''
最后，理解变量在计算机内存中的表示也非常重要。当我们写：a = 'ABC'时，Python解释器干了两件事情：
在内存中创建了一个'ABC'的字符串；
在内存中创建了一个名为a的变量，并把它指向'ABC'。
也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
'''

'''
数据类型
计算机顾名思义就是可以做数学计算的机器，因此，计算机程序理所当然地可以处理各种数值。但是，计算机能处理的远不止数值，还可以处理文本、
图形、音频、视频、网页等各种各样的数据，不同的数据，需要定义不同的数据类型。在Python中，能够直接处理的数据类型有以下几种：
整数、浮点数、字符串、布尔值、空值
'''
