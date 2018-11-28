# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
while True:
    # 用户输入字符
    c = input("请输入单个字符: ")
    # 判断字符长度
    if len(c)>=2:
        # 打印提示信息
        print("字符长度超出范围，请输入单个字符！")
    else:
        # 打印ASCII 码
        print(c + " 的ASCII 码为", ord(c))
