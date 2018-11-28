import pymysql

def init_db():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "mrsoft", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    return db,cursor

def show_menu():
    menu = """菜单：
    0.退出系统    
    1.根据销售额降序
    2.根据销售额升序
    3.根据百分比降序
    4.根据百分比升序
    """
    print(menu)

def rank(field,order):
    """
    根据字段进行排序
    :param field: 字段名
    :param order: 排序方式
    """
    db,cursor = init_db()   # 初始化pymysql
    sql = 'select * from ecommerce order by {0} {1}'.format(field,order) # 查询的SQL语句
    cursor.execute(sql)     # 执行SQL语句
    results = cursor.fetchall() # 查找所有数据
    db.close()              # 关闭db
    # 输出结果
    for result in results:
        print('商家：{0} | 销量：{1} | 占比：{2}%'.format(result[1],result[2],result[3]) )

if __name__ == "__main__":
    show_menu() # 展示菜单
    num = int(input('请输入相应操作菜单：'))
    # 根据菜单执行相应操作
    while num != 0:
        if num == 1:
            rank('sale','desc')
        elif num == 2:
            rank('sale','asc')
        elif num == 3:
            rank('percent','desc')
        elif num == 4:
            rank('percent','asc')
        else:
            print('输入错误，请参照菜单提示')
        num = int(input('请输入相应操作菜单：'))
    print('您已成功退出系统')



