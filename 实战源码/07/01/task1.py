# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
from random import choice  # 随机模块

cut = [0.09, 0.03, 0.08, 0.06]  # 随机砍价的列表
price = 4000  # 总价
while True:
    print("当前商品价格为",price,"元！")
    input("单击“Enter”砍一刀！")
    if price<=800:
        print("不能再砍了，要不商家该赔的穿不起衣服了！")
        break
    price = price-4000 * choice(cut) # 计算砍价后的价格


