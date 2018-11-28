# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
i = int(input("请输入您乘坐的出租车共行驶了多少公里？"))
if i <= 3:
    print("您好乘客！行驶的公里数在起步价范围内，请支付10元！")
if i > 3 and i < 13:
    price = (i - 3) * 2 + 10
    print("您好乘客！行驶的公里数已超出起步价格，请支付", price, "元！")
if i > 13:
    price = (i-13)*3+30
    print("您好乘客！行驶的公里数已超出13公里，请支付", price, "元！")