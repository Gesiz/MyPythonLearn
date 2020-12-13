import pymysql
import json
# 参数列表
func_list = {}
# /index.html:index
# /center.html:center


# path = /index.html
def route(path):

    def func_out(func):
        # index.html
        func_list[path] = func
        def func_in():
            func()

        return func_in

    return func_out

# "/index.html":index,
# "/center.html":center


@route("/index.html")  # 1 route('index.html')  2 @func_out ==> index = func_out(index)
def index():
    with open("./template/index.html") as f:
        content = f.read()

    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='mysql',
                           database='stock_db',
                           charset='utf8')

    cur = conn.cursor()
    sql = "select * from info;"
    cur.execute(sql)
    # 数据库中的数据（元组）
    stock_data = cur.fetchall()

    cur.close()
    conn.close()

    template = """
            <tr>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <th>%s</th>
                 <th>%s</th>
                 <th>%s</th>
                 <th>%s</th>
                 <th>%s</th>
            </tr>

            """
    html = ""

    for i in stock_data:
        html += template % (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[7])

    content = content.replace("{%content%}",html)

    return content


@route("/center.html")
def center():
    with open("./template/center.html") as f:
        content = f.read()

    content = content.replace("{%content%}","11111111")
    return content


@route("/center_data.html")
def center_data():
    conn = pymysql.connect(host='localhost', port=3306, database='stock', user='root', password='mysql', charset='utf8')
    # 创建游标
    cursor = conn.cursor()

    # 执行sql语句
    sql = "select *  from info inner join focus on info.id=focus.id;"
    cursor.execute(sql)

    # 获取数据 元组  ((),())
    stock_data = cursor.fetchall()

    # 把元组转化成列表
    center_data_list = [{"code": row[1],
                         "short": row[2],
                         "chg": row[3],
                         "turnover": row[4],
                         "price": str(row[5]),
                         "highs": str(row[6]),
                         "note_info": row[9]} for row in stock_data]

    # 把列表转化成json字符串
    json_str = json.dumps(center_data_list)

    # 关闭连接
    cursor.close()
    conn.close()

    return json_str


# func_list["/index.html"] = index
# func_list["/center.html"] = center


# 框架的接口
def application(request_path):
    try:
        func = func_list[request_path]
        # index()
        ret = func()
        return ret
    except Exception as e:
        print(e)
        return "404 not found"