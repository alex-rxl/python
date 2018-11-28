# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
contacts = {"阿童木","阿龙","彤彤","秋秋","Rexx","space"}
while True:
    i = input("请选择需要的功能！"
              "\n1.查询所有联系人"
              "\n2.添加联系人"
              "\n3.删除联系人"
              "\n4.退出")
    # 查询所有联系人
    if i == "1":
        for c in contacts: # 遍历联系人
            print(c)        # 打印所有的联系人

    # 添加联系人
    if i == "2":
        name = input("请输入添加的联系人姓名！")
        contacts.add(name)
    # 删除联系人
    if i == "3":
        name = input("请输入需要删除的联系人姓名！")
        if name in contacts:      # 判断通讯录中是否有想要删除的联系人
            contacts.remove(name) # 删除指定的联系人
        else:
            print("通讯录中并没有该",name,"联系人！")

    # 退出
    if i == "4":
        break

