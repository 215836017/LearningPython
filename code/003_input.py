#!/usr/bin/env python3

# 标题: Python中的键盘输入

print('Python提供了一个input()，可以让用户从键盘进行输入')

'''
1. Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字,
当你输入name = input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入。
2. input()可以让你显示一个字符串来提示用户
'''
print("please input: ")
name = input()
print('name is', name)

nameAgain = input('please input your name again: ')
print('you name is', nameAgain)
