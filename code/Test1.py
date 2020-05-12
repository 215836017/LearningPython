print('hello python')
'''
标题：第一个Python程序
'''


'''
1. 绝对不能用Word和Windows自带的记事本。Word保存的不是纯文本文件，而记事本会自作聪明地在文件开始的地方加上几个特殊字符（UTF-8 BOM），
结果会导致程序运行出现莫名其妙的错误。


3. 直接运行py文件
 能不能像.exe文件那样直接运行.py文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在.py文件的第一行加上一个特殊的注释：

#!/usr/bin/env python3
print('hello, world')

然后，通过命令给hello.py以执行权限：
$ chmod a+x hello.py

就可以直接运行hello.py了，比如在Mac下运行：
./hello.py

'''


'''
1. 注意print前面不要有任何空格

2. print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
'''
print('abcdef', '12345','hhhhh')
# 打印结果： abcdef 12345 hhhhh

print(100)
print(100 + 200)
print(100 - 200)
print('100 + 200 = ', 100 + 200)   # 这个格式比较美观

'''
1. Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字,
当你输入name = input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入。
2. input()可以让你显示一个字符串来提示用户
'''
print("please input: \n")
name = input()
print('name is', name)

nameAgain = input('please input your name again: ')
print('you name is', nameAgain)