# 框架的接口
def application(request_path):
    if request_path == "/center.html":
        # 应答体
        # xxx
        return "center"
    elif request_path == "/index.html":
        # xxx
        return "index"
    else:
        return "error"