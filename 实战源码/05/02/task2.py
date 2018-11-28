# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
number_list = [] # 保存输入的数字
result = 0       # 定义计算结果的变量
while True:
    i = input("输入需要相加的数字！")
    number = int(i)  # 转换为整数类型
    number_list.append(number) # 将输入的数字添加至列表当中
    if len(number_list) == 3:  #判断列表长度
        for n in number_list: # 遍历列表中的数字
            result = result + n # 相加计算
        print("计算结果为：",result)           # 打印结果
        break                  # 跳出循环
