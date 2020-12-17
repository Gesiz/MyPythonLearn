import json
import time

import pymysql

# 函数列表
func_list = {}


# 路由装饰器
def route(path):
    def func_out(func):
        func_list[path] = func

        def func_in():
            func()

        return func_in

    return func_out


@route("/index.html")
def index():
    with open("./template/index.html", encoding="utf-8") as f:
        content = f.read()
    conn = pymysql.connect(host="localhost",
                           # port=33060,
                           user="root",
                           password="mysql",
                           database="stock_db",
                           charset="utf8"
                           )
    cur = conn.cursor()

    # 查询sql语句
    sql = "select * from info;"
    # 执行sql
    cur.execute(sql)
    # 获取结果集
    stock_data = cur.fetchall()

    cur.close()
    conn.close()

    temp = """
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <th><input type="button" value="添加"></input></th>
                </tr>
            """
    html = ""
    # 元组形式的股票数据
    # ((1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18),)
    for i in stock_data:
        html += temp % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

    content = content.replace("{%content%}", html)

    return content


@route("/center.html")
def center():
    with open("./template/index.html", encoding="utf-8") as f:
        content = f.read()
    return content


@route("/ajax.html")
def ajax():
    my_data = {'time':str(time.time())}
    my_data = json.dumps(my_data)
    return my_data

def application(request_path):
    # if request_path == "/index.html":
    #     return index()
    # elif request_path == "/center.html":
    #     return center()
    # else:
    #     return "not found"
    try:
        func = func_list[request_path]
        return func()
    except Exception as e:
        print(e)
        return "not found"
