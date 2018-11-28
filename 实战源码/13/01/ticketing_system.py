import prettytable as pt

def show_tickt(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ["行号","座位1", "座位2", "座位3", "座位4","座位5"]
    for i in range(row_num):
        l = ["第{}行".format(i+1), "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(l)
    print(tb)

def order_tickt(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ["行号","座位1", "座位2", "座位3", "座位4","座位5"]
    for i in range(row_num):
        if int(row) == i + 1:
            l = ["第{}行".format(i + 1), "有票", "有票", "有票", "有票", "有票"]
            l[int(column)] = '已售'
            tb.add_row(l)
        else:
            l = ["第{}行".format(i+1), "有票", "有票", "有票", "有票", "有票"]
            tb.add_row(l)
    print(tb)

if __name__ == "__main__":
    row_num = 13        # 共13行
    show_tickt(row_num) # 显示空座
    choose_num = input('请输入选择的座位，如13,5，表示第13排5号座位：')
    try:
        row,column = choose_num.split(',') # 拆分行数和列数
    except:
        print('输入格式错误，如选择第13排5号座位请输入：13,5')
    order_tickt(row_num) # 显示订票

