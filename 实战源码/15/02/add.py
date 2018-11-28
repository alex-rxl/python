import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "mrsoft",charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 数据列表
data = [("聚美优品",58,0.16),
("京东",12945,36.3),
("亚马逊中国",391,1.1),
("当当网",357,1.0),
("唯品会",728,2.0),
('考拉严选 ',116,0.3),
('天猫',21086,59.1)
]
try:
    # 执行sql语句， 插入多条数据
    cursor.executemany("insert into ecommerce(name, sale, percent)values( % s, % s, % s)", data)
    # 提交数据
    db.commit()
except Exception:
    print("发生异常", Exception)
    # 发生错误时回滚
    db.rollback()
    # 关闭数据库连接

db.close()
