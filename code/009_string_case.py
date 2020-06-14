print('字符串内建函数')

# 字符串的大小写

message = 'today is Sunday'
msg = message.capitalize()  # 将字符串的第一个字符转为大写
print('message.capitalize = ', msg)

msg = message.title()  # 将字符串中每个单词的首字母大写
print('message.title = ', msg)
print('message.istitle = ', message.istitle())
print('msg.istitle = ', msg.istitle())

msg = message.upper()  # 将字符串全部字母大写
print("message.upper = ", msg)

msg = message.lower()  # 将字符串的全部字母小写
print("message.lower = ", msg)
