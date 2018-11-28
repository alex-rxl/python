# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2018/10/9  13:45
# 文件名称   ：task2.py.py
# 开发工具   ：PyCharm
year = [89,98,00,75,68,37,58,90] # 原有的年份列表
for index,value  in enumerate(year):  # 遍历列表元素索引与年份
      if str(value)!='0':             # 判断非0年份
            year[index]=int('19'+str(value))
      else:
            year[index]=int('200'+str(value)) # 判断2000年
print(year) # 打印修改后的年份列表

