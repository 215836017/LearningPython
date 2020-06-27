print('通用的序列操作 -- 成员资格')

'''
1. 要检查特定的值是否在序列中，可使用运算符in。
   运算符in检查是否满足指定的条件，并放回Boolean值。
'''

name = ['aaa', 'Python', 123, ['aaa', 123]]
name1 = ['aaa', 123]
text = 'text_text_123'

print("'aaa' in name = ", 'aaa' in name)
print("'123' in name = ", '123' in name)
print("'123' in name = ", 123 in name)
print("'t_t' in name = ", 't_t' in name)
print("'t_t' in text = ", 't_t' in text)
print("'123' in text = ", '123' in text)
print('name1 in name', name1 in name)
print('name in name1', name in name1)
# print("123 in text = ", 123 in text) #报错：TypeError: 'in <string>' requires string as left operand, not int
'''
打印结果：
'aaa' in name =  True
'123' in name =  False
'123' in name =  True
't_t' in name =  False
't_t' in text =  True
'123' in text =  True
name1 in name True
name in name1 False
'''
