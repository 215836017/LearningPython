#!/usr/bin/env python3

# 标题: Python中的语句

print(range(8))
print(range(0, -10, -1))

'''
1. 最简单的for结构如下：
'''
print('\n\ntest 11111111')
for i in range(20):
    print('test for: ', i)

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
