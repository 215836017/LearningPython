# 测试读和写

f1 = open("aa.txt", 'a')

f1.write("adb")
f1.close()

f2 = open("aa.txt", 'r')
print(f2.read())


# f3 = open("F:\python_works\myTest\\files\\adc.txt")
f3 = open("..\\files\\adc.txt")
print(f3.read())