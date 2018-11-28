# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
number = [58,12945,391,357,728,116,21086]  # 原有的销量列表排序
for index,value  in enumerate(number):  # 遍历列表元素索引与销量
    number[index]=int(value+value*0.4)        # 修改销量列表增加%40以后的销量
number.sort(reverse=True)            # 进行降序排列
print(number)                         # 打印降序销量列表


