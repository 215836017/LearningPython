print('循环')

'''
标题：循环
Python的循环有两种，一种是for...in循环, 另一种循环是while循环
'''

classmates = ['abc', '123', 'def', '456', 'ghj', '789']
for str in classmates:
    print(str)


sum = 0
for x in range(101):
    sum += x
print('sum =', sum)


sum1 = 0
while sum1 <100:
    sum1 += 1
print('sum1 =', sum1)


'''
1. 在循环中，break语句可以提前退出循环
2. 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
'''