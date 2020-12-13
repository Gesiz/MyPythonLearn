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

    content = content.replace("{%content%}","stock_db")

    return content


@route("/center.html")
def center():
    with open("./template/center.html") as f:
        content = f.read()
    return content



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