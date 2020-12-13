# 参数列表
func_list = {}

# "/index.html":index,
# "/center.html":center

def index():
    with open("./template/index.html") as f:
        content = f.read()

    return content


def center():
    with open("./template/center.html") as f:
        content = f.read()
    return content


def error():
    return "error"

func_list["/index.html"] = index
func_list["/center.html"] = center


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