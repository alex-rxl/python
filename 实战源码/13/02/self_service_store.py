import prettytable as pt  # 请先安装prettytable模块

tb = pt.PrettyTable()
tb.field_names = ["食品名称","价格"]
tb.add_row(['康师傅方便面','3.5 元'])
tb.add_row(['农夫山泉矿泉水','2 元'])
tb.add_row(['伊利纯牛奶','2.4元'])
tb.add_row(['金锣火腿肠','5元'])
print(tb)