from math import pi
from math import e

"""注：基于python3.7.0"""

'一、 字符串基本操作'
'所有标准序列操作(索引、切片、乘法、成员资格检查、长度、最小值和最大值)都适用于字符串'
str = "abcdef1234.HHHH"
print('str[0] = ', str[11])

'但是字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的'
# str[2] = 'WW'   # 运行后报错：Traceback (most recent call last):
# print('str = ', str)

'二、 设置字符串的格式'
'以前主要的解决方案是使用字符串格式设置运算符----百分号。在%左边指定一个字符串(格式字符串)，并在右边指定要设置其格式的值。'
'指定格式的值时，可以使用单个值(如字符或数字)，可以使用元组(如果要设置多个值)，还可以使用字典。'
strFromat = 'Hello, %s, %s enouth for you?'
strValues = ("Python", 'Hot')
print("str format:", strFromat % strValues)

'设置字符串的格式这里主要是对字符串调用format方法，并提供要设置其格式的值：'
'(1). 替换字段名：在最简单的情况下，只需要向format提供要设置其格式的未命名参数，并在格式字符串中使用未命名字段。'
' 最简单的情况下，替换字段没有名称或索引'
str1 = '{}, {} and {}'.format('First', 'Second', 'Third')
print('str1:', str1)

'将索引用作名称'
str2 = '{2}, {1} and {0}'.format('First', 'Second', 'Third')
print('str2:', str2)

'索引不需要按顺序排序'
str3 = '{1}, {2} and {0}'.format('First', 'Second', 'Third')
print('str3:', str3)

' 不能同时使用手工编号和自动编号，因为这样很快会变得混乱不堪'
# str4 = '{1}, {} and {0}'.format('First', 'Second', 'Third')
# print('str4:', str4) #运行后报错：ValueError: cannot switch from manual field specification to automatic field numbering

' 指定参数名称'
str5 = '{foo} {} {bar} {}'.format(1, 2, bar=4, foo=3)
print('str5:', str5)

str5_1 = '{name} is approximately {value}'.format(value=pi, name='π')
print('str5_1:', str5_1)
str5_2 = '{name} is approximately {value:.2f}'.format(value=pi, name='π')
print('str5_1:', str5_2)

'参数名称和索引混合使用'
str6 = '{foo} {1} {bar} {0}'.format(1, 2, bar="bar", foo='foo')
print('str6:', str6)

'并非只能使用提供的值本身，而是可以访问其组成部分'
fullName = ['Alfred', 'Smoketoomuch']
str7 = "Mr {name[1]}".format(name=fullName)
print('str7:', str7)

'在Python3.6及以后版本中，如果变量与替换字段同名，还可以使用简写：使用f字符串----即在字符串前面加f'
str8 = f"Euler's constant is roughly {e}"
print('str8:', str8)
str9 = "Euler's constant is roughly {e}".format(e=e)
print('str9:', str9)
