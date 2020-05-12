#!/usr/bin/env python3

# 标题: 学习Python中的打印语句


'''
简单打印
1. 注意print前面不要有任何空格
2. print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出，并且逗号的地方会用空格代替：
3. print()函数也可以向Java中的print()一样，用"+"连接，这样的话打印出的结果不会有空格
4. print()函数自身就会自动换行，不需要再加 \n 了
'''

print(100)
print(100 + 200)
print(100 - 200)
print('100 + 200 = ', 100 + 200)   # 这个格式比较美观
# 打印结果：100
# 打印结果：300
# 打印结果：-100
# 打印结果：100 + 200 =  300


print('abcdef', '12345', 'hhhhh')
print('abcdef' + '12345' + 'hhhhh')
# 打印结果： abcdef 12345 hhhhh
# 打印结果：abcdef12345hhhhh
a = 1
b = 2
a = a ^ b
b = a ^ b
a = a ^ b
print('exchange: a=%d' % a + ',b=%d' % b)

'''
使用format：
1. 格式为 “{}”format(...) ----{}其实是set
2. format有很丰富的用法
'''
# 1. 按顺序给参数
print('{} is a Chinese, He(or She) is {} years old, and salary is {} yuan'.format("xiaoMing", 30, 8888.88))
print("{} is a Chinese, He(or She) is {} years old, and salary is {} yuan".format("Jack", 20, 666.66))
# TODO 注意：format前面是点号，不是逗号
# 打印结果：xiaoMing is a Chinese, He(or She) is 30 years old, and salary is 8888.88 yuan

# 2. 不按顺序给参数
a = 3
b = 3.2
print('exchange: a = {1}, b = {0}'.format(a, b))

# 3. 在format中设置参数
print('网站名称:{name}, 网站地址:{address}'.format(name='Python官网', address="https://www.python.org"))

# 4. 数字格式化
PI = 3.1415926
print("PI = {:.3f}".format(PI))
'''
数字	       格式	         输出	            描述
3.1415926	   {:.2f}	     3.14	         保留小数点后两位
3.1415926	   {:+.2f}	     +3.14	         带符号保留小数点后两位
-1	           {:+.2f}	     -1.00	         带符号保留小数点后两位
2.71828	       {:.0f}	     3	             不带小数
5	           {:0>2d}	     05	             数字补零 (填充左边, 宽度为2)      
5	           {:x<4d}	     5xxx	         数字补x (填充右边, 宽度为4)
10	           {:x<4d}	     10xx	         数字补x (填充右边, 宽度为4)
1000000        {:,}	         1,000,000	     以逗号分隔的数字格式
0.25	       {:.2%}	     25.00%   	     百分比格式
1000000000	   {:.2e}	     1.00e+09	     指数记法
13	           {:>10d}	         13	         右对齐 (默认, 宽度为10)
13	           {:<10d}	     13	             左对齐 (宽度为10)
13	           {:^10d}	       13	         中间对齐 (宽度为10)
'''

# 5. 进制
print('进制:')
print('{:b}'.format(11))  # 1011
print('{:d}'.format(11))  # 11
print('{:o}'.format(11))  # 13
print('{:x}'.format(11))  # b
print('{:#x}'.format(11))  # 0xb
print('{:#X}'.format(11))  # 0XB

'''
总结：
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
b、d、o、x 分别是二进制、十进制、八进制、十六进制
'''

# 6. 使用大括号 {} 来转义大括号{}
print("{} 对应的位置是 {{0}}".format("string", "int", 'float'))
print("{2} 对应的位置是 {{2}}".format("string", "int", 'float'))
