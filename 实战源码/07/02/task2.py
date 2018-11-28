# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
from random import choice  # 随机模块
while True:
    commodity =["康师傅","康帅傅"]   # 随机购买的商品
    i = input("单击“Enter”键，随机购买商品！")
    i = choice(commodity)            # 随机购买商品
    if i=="康师傅":
        print("恭喜您买到了真的康师傅！")
    else:
        print("真的很同情您，您买到了假货，这是康帅傅！")
