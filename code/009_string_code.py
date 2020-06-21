print('字符串的编解码')

'''
1. 内建函数--编解码： encode  decode
'''
msg = '我是一条中文消息'

result = msg.encode('utf-8')
print(result)
'''
打印结果为：
b'\xe6\x88\x91\xe6\x98\xaf\xe4\xb8\x80\xe6\x9d\xa1\xe4\xb8\xad\xe6\x96\x87\xe6\xb6\x88\xe6\x81\xaf'
'''

msg1 = result.decode('utf-8')
print(msg1)

'''
2. 内建函数： startswith()  endswith()
'''
name = 'abcdefg123'
print('name.startswith("ab")', name.startswith('ab'))
print('name.startswith("fg")', name.startswith('fg'))
print('name.endswith("fg")', name.endswith('fg'))
print('name.endswith("123")', name.endswith('123'))
