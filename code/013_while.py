#!/usr/bin/env python3

# 标题: Python中的while语句
print('学习while')
'''
1. 使用while循环时需要先定义一个变量用来执行条件判断
'''
print('\ntest 1111111111')
i = 0
while i < 10:
    print("i = ", i)
    i += 1

'''
2. while 也可以结合else分支
'''
print('\n\ntest 2222222222')
sum = 0
while sum < 100:
    sum += 1
else:
    print('完成求和了...')
print('sum =', sum)

'''
3. while和break结合使用
'''
print('\n\ntest 3333333')
i = 0
while i < 10:
    if i < 5:
        print('i =', i)
    else:
        print('test break')
        break
    i += 1
else:
    print('while finish...')
'''
打印结果：
i = 0
i = 1
i = 2
i = 3
i = 4
test break
'''
# TODO 同for-else结果相同，while正常结束时while-else的else分支才会进入。
# TODO 同for-else结果相同，while由break等异常结束时while-else的else分支 不 不 不会进入。
