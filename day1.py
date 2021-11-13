"""
Day2-语言元素

Version：0.1
Author：吴振宇
"""

# 使用变量保存数据并进行加减乘除运算
a = 321
b = 12
print(a + b)    # 333
print(a - b)    # 309
print(a * b)    # 3852
print(a / b)    # 26.75

# 使用type()检查变量的类型
a = 100
b = 12.345
c = 1 + 5j
d = 'Hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 使用input()函数获取键盘输入(字符串)
# 使用int()函数将输入的字符串转换成整数
# 使用print()函数输出带占位符的字符串
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# 赋值运算符和复合赋值运算符
a = 10
b = 3
a += b     # a = a + b   
a *= a+2   # a = a * (a + 2)
print(a)

# 比较运算符和逻辑运算符的使用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False

# 华氏温度转换为摄氏温度
f = float(input('请输入华氏温度：'))
c = (f -32) / 1.8
print('%.1f华氏温度 = %.1f' % (f, c))

# 计算园周长和面积
r = float(input('请输入圆的半径：'))
l = 2 * 3.14 * r
s = 3.14 * r * r
print('周长：%.2f' % l)
print('面积：%.2f' % s)

# 判断是否是闰年
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)