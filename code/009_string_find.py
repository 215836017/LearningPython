print('字符串内建函数')

# 字符串的查找和替换
'''
find()  rfind() lfind() index() rindex() lindex() replace()
'''

s = 'index luchhh lucky gossd'

result = 'R' in s
print('R in s = ', result)

result = s.find('R')
print('s.find(R) = ', result)  # 返回值为-1表示没有找到

result = s.find('l')
print('s.find(l) = ', result)  # 如果找到，则返回第一次找到的位置

result = s.find('l', result + 1)  # 指定位置来查找
print('s.find(l) 2222 = ', result)  # 如果找到，则返回第一次找到的位置

result = s.rfind('go')
print("s.rfind('go') = ", result)

result = s.replace('hhh', 'HHH')
print('s.replace 11111 = ', result)

result = s.replace(' ', '', 4)
print('s.replace 2222 = ', result)