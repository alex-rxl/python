# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
str = input("是否向外透露了继承事件：（已透露/未透露）")
if str == "未透露":
      money =int(input("一个月内所花钱数（单位亿元）:"))
if money >= 10:
      print("获得百亿继承权")
else:
      print("失去百亿继承权")
if str == "已透露":
      print("失去百亿继承权")


