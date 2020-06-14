#!/usr/bin/env python3

# 标题: Python中的for语句

print(range(8))
print(range(0, -10, -1))

'''
1. Python的循环有两种，一种是for...in循环, 另一种循环是while循环
最简单的for结构如下：
'''
print('\n\ntest 11111111')
sum = 0
for i in range(20):
    print('test for: ', i)
    sum += 1
print('sum1 =', sum)

for i in range(10, 20, 2):
    print('test for:', i)

'''
2. for-else 结构
'''
print('\n\ntest 22222222')
for i in range(3):
    print('test for: ', i)
else:
    print('test else')
'''
打印结果为：
test for:  0
test for:  1
test for:  2
test else
'''
'''
for-else中的else分支表示for循环执行完了之后的逻辑
'''

'''
3. 结合pass使用
'''
print('\n\ntest 3333333333')
for i in range(10):
    if i < 5:
        pass
    else:
        print('Hello', i)
else:
    print('for loop finish')
'''
Hello 5
Hello 6
Hello 7
Hello 8
Hello 9
for loop finish
'''

'''
4. 结合break使用
'''
print('\n\ntest 44444444')
for i in range(3):
    userName = input('please input userName:')
    pwd = input('please input password:')
    if userName == 'admin' and pwd == '123456':
        print('Welcome admin!!!')
        break
    else:
        print('userName or password is invalid, please input again')
else:
    print('账户被锁定，需要重新激活！')
# TODO 经过测试可知：如果for是正常完成时，会进入到for-else结构的else分支。
# TODO 当使用break跳出for循环后，for-else中的else分支也不会再进入了

'''
5. 遍历列表
'''
print('\n\ntest 5555555555')
classmates = ['abc', '123', 'def', '456', 'ghj', '789']
for s in classmates:
    print(s)

'''
6. 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
'''
print('\n\ntest 6666666666666')
for i in range(20):
    if i / 2 == 0:
        continue
    else:
        print('i = ', i)
