print("Hello World, Hello Python.");

print('Hello World!!! Hello Python!!!')

print("总结：")
print("1. Python中行尾分号可有可无，Python中默认不加分号----换行即一行结束")
print("2. Python中的字符串：单引号和双引号都可以,但是要配对，不能胡乱嵌套")
print("3. 每一行的开头不能随意加空格，因为Python是根据每一行开始的缩进来识别代码结构的----即Python中行开头的空格类似于Java中的{}")


'''
注释：
1. 单行注释：在开头加 #
2. 多行注释：用三引号包裹多行
'''


'''
注意事项：
1. 绝对不能用Word和Windows自带的记事本。Word保存的不是纯文本文件，而记事本会自作聪明地在文件开始的地方加上几个特殊字符（UTF-8 BOM），
结果会导致程序运行出现莫名其妙的错误。
2. 直接运行py文件: 能不能像.exe文件那样直接运行.py文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在.py文件的第一行
加上一个特殊的注释，如下所示的第一行：
#!/usr/bin/env python3
print('hello, world')

然后，通过命令给hello.py以执行权限：
$ chmod a+x hello.py

就可以直接运行hello.py了，比如在Mac下运行：
./hello.py
'''

print('Hello Python: A happy beginning!')
