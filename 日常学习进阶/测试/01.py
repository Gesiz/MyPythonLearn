# DROP DATABASE heima;
# CREATE DATABASE heima CHARSET=UTF8;
# use heima;
# CREATE TABLE goods(
# id int primary KEY auto_increment,
# name VARCHAR(20) not NULL unique,
# price DECIMAL(7,2)
# )
#
# INSERT INTO goods VALUES(0,"神州笔记本",3000)



import pymysql


class ShopManager:

    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",
                                    user="root",
                                    password="mysql",
                                    database="heima",
                                    charset="utf8"
                                    )
        self.cur = self.conn.cursor()

    def addSql(self, name, price):
        sql = f'INSERT INTO goods VALUES(0,"{name}",{price})'
        self.cur.execute(sql)
        self.conn.commit()

    def searchSql(self, name):

        sql = f'select * from goods where name = "{name}";'
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def addThing(self, name, price):
        try:
            data = self.searchSql(name)
        except Exception as e:
            print("您输入的数据可能存在问题 请重新输入",e)
        if bool(data):
            print("商品已存在，请重新添加")
        else:
            self.addSql(name, price)
            print("添加成功")

    def searchThing(self, name):
        data = self.searchSql(name)
        if bool(data):
            print(f"商品编号:{data[0][0]} 商品名称:{data[0][1]} 商品价格:{data[0][2]}")
        else:
            print("商品名称错误 请重新输入")

    def __del__(self):
        self.cur.close()
        self.conn.close()


msg = """-------商品管理系统-------
1: 添加商品
2: 查询商品
请输入功能对应的序号:"""
if __name__ == '__main__':
    Mana = ShopManager()
    while True:
        rev = input(msg)
        if rev == "1":
            name = input("请输入商品的名称:")
            price = input("请输入商品的价格:")
            Mana.addThing(name, price)
        elif rev == "2":
            name = input("请输入商品的名称:")
            Mana.searchThing(name)
        else:
            print("您输入的有问题哦 请重新输入")
