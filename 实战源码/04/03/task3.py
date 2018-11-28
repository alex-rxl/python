# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
str =""     # 定义连接后的字符串
while True:
    # 用户输入ASCII码，将输入的数字转换为int类型
    a = int(input("请输入一个ASCII码: "))
    str = str + chr(a) # 连接字符串
    print(str)         # 打印连接后的字符串

