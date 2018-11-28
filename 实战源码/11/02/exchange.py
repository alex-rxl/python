def exchange(money):
    return money* 9.912

if __name__  == "__main__":
    money = float(input('请输入要转化的人民币,退出输入0：'))
    while money:
        print('{0}元人民币={1}俄罗斯卢布'.format(money,exchange(money)))
        money = float(input('请输入要转化的人民币,退出输入0：'))