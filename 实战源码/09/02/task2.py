# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
i = int(input("请输入购买手机的总价格！"))
i = i/6+i*0.006 # 计算每个月加上总价利息应还的钱数
print(i)        # 打印每个月应还的钱数
