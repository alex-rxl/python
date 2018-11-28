# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
# 答案
"""
S 的ASCII 码为 83
t 的ASCII 码为 116
a 的ASCII 码为 97
y 的ASCII 码为 121
空格的ASCII 码为 32
h 的ASCII 码为 104
u 的ASCII 码为 117
n 的ASCII 码为 110
g 的ASCII 码为 103
r 的ASCII 码为 114
y 的ASCII 码为 121
, 的ASCII 码为 44
S 的ASCII 码为 83
t 的ASCII 码为 116
a 的ASCII 码为 97
y 的ASCII 码为 121
空格的ASCII 码为 32
f 的ASCII 码为 102
o 的ASCII 码为 111
o 的ASCII 码为 111
l 的ASCII 码为 108
i 的ASCII 码为 105
s 的ASCII 码为 115
h 的ASCII 码为 104
. 的ASCII 码为 46
"""
str =""     # 定义连接后的字符串
while True:
    # 用户输入ASCII码，将输入的数字转换为int类型
    a = int(input("请输入一个ASCII码: "))
    str = str + chr(a) # 连接字符串
    print(str)         # 打印连接后的字符串

