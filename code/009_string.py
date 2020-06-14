print('字符串和编码')
'''
标题：字符串和编码
'''

'''
字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。
    因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，
一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大
整数是65535，4个字节可以表示的最大整数是4294967295。由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是
大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。
    但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。
你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，
结果就是，在多语言混合的文本中，显示出来会有乱码。因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
    Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数
编程语言都直接支持Unicode。
'''

'''
1. ASCII编码是1个字节，而Unicode编码通常是2个字节：
字母A用ASCII编码是十进制的65，二进制的01000001；
字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

2. 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码
需要多一倍的存储空间，在存储和传输上就十分不划算。

所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。

UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，
只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
4. UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的软件可以在UTF-8编码下继续工作
5. 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
6. 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
'''

'''
1. 如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
2. 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：'I\'m \"OK\"!'  表示 I'm "OK"!
3. 字符\本身也要转义，所以\\表示的字符就是\
4. 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
5. 三引号的使用： 如果赋值给了变量，则是一个字符串；如果没有赋值给变量，则表示连续的多行注释
6. 三引号如果内容有换行的话，占用的内存和单双引号占用的内存不同
'''
print('\t 12333')
print(r'\n\n\t \12344')

testThree1 = '''
abcdef
12345
==__==
'''
testThree2 = '''
abcdef\tghijk
12345\n678
==__==
'''
testThree3 = r'''
abcdef\tghijk
12345\n678
==__==
'''
print(testThree1)
print(testThree2)
print(testThree3)

'''
1. 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
2. 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
3. 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换
4. 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

5. 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
6. 在Python中，采用的格式化方式和C语言是一致的，用%实现字符串的格式化
7. 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
'''
print('Hello %s, hello %s, I have money $%d' % ('小明', '小红', 50000))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

'''
1. 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
2. 要计算str包含多少个字符，可以用len()函数
3. len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
'''
print('字母A对应的整数:', ord('A'))
print('字母\"中\"对应的整数:', ord('中'))
print('整数66对应的字母：', chr(66))
print('整数25991对应的字母：', chr(25991))

'''
4. 字符串的比较
   == 比较的是内容
   is 比较的是地址
'''
print('\n\ntest 4444444444')
s1 = 'abc'
s2 = 'abc'
print('s1 == s2: ', s1 == s2)
print('s1 is s2: ', s1 is s2)
'''
s1 == s2:  True
s1 is s2:  True
'''

# s3 = input('input s3:')
# s4 = input('input s4:')
# print('s3 == s4: ', s3 == s4)
# print('s3 is s4: ', s3 is s4)
'''
输入s3和s4相同的字符串：
s3 == s4:  True
s3 is s4:  False
'''

'''
5. 字符串运算符 +
'''
print('\n\ntest 5555555555')
print('s1 + s2 =', s1 + s2)

'''
6. 运算符 *
'''
print('\n\ntest 666666666')
print('s1 * 4 = ', s1 * 4)
'''
7. 关键字 in
'''
print('\n\ntest 77777777777')
name = 'python'
result = 'th' in name
print(result)

'''
8. 使用字符串的下标 []
'''
print('\n\ntest 888888888888')
print(name[3])
print(name[0:3])  # 切片：包前不抱后
print(name[2:5])  # 切片：包前不抱后
print(name[2:])  # 切片：包前不抱后
print(name[:5])  # 切片：包前不抱后
print(name[:])  # 切片：包前不抱后
print(name[2:-1])  # 切片：包前不抱后
print(name[-3:-1])  # 切片：包前不抱后
print(name[-1:])  # 切片：包前不抱后
print(name[-1:0])  # 切片：包前不抱后
print(name[-1:-5])  # 切片：包前不抱后
'''
打印结果：
h
pyt
tho
thon
pytho
python
tho
ho
n
 (空的)
 (空的)
'''

'''
9. 实现倒序输出
'''
print('\n\ntest 99999999999')
print(name[::-1])
'''
打印结果：
nohtyp
'''
