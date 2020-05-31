"""注：基于python3.7.0"""

'1. 单引号字符串以及对引号转义'
'Python中打印字符串时，用单引号和双引号的效果是一样的。但是，单引号或者双引号必须是配对的，一半单引号和一半双引号的写法是不对的'
print("Hello, World!")
print('Hello, World!')
# print('Hello, World!")  #编译器直接报错

'为何同时支持单引号和双引号呢？因为在有些情况下会引号是字符串中的一部分，也需要打印出来'
print("Let's go!")
print('"Hello,world!"she said')

'上面的两个例子只是出于方便的写法而已，如果有时候需要通过将单引号和双引号都打印出来，那么看使用反斜杠对引号进行转义即可'
print('Let\'s go!')
print("\"Hello,world!\"she said")

'2. 拼接字符串'
'拼接字符串就像将数相加一样，用加号连接起来就可以了'
x = 'Hello, '
y = "Python"
print(x + y)

'3. 字符串表示str和repr'
' 使用str能以合理的方式将值转换成用户能看懂的字符串'
print(str('Hello, \nworld!'))

'使用repr通常会获得值的合法Python表达式表示'
print(repr('Hello, \nworld!'))

