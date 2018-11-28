class Cost:
    def __init__(self,price,num):
        self.price = price
        self.num = num
    def sum(self):
        sum = self.price * self.num
        return sum

if __name__ == "__main__":
    price = float(input('请输入格列卫的单价:'))
    num = int(input("请输入购买数量:"))
    cost = Cost(price,num)
    sum = cost.sum()
    print('格列宁单价是{0}元，购买{1}盒共花费{2}元'.format(price,num,sum))