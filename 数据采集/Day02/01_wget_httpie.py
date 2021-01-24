"""
wget
    -O 以指定文件名保存下载的文件 wget -O test.png http://httpbin.org/image/png
    --limit-rate=200k  限速下载   wget --limit-rate=200k -c https://ks-xpc15.xpccdn.com/b2fe7c20-c06d-4837-8776-ac426ce57583.mp4
    -c 断点续传
    -b 在后台下载
    -U 设置 User-Agent
    --mirror 镜像某个网站
    -p 下载页面中所有相关的资源
    -r 递归下载所有的链接
                            镜像下载整个网站并下载到本地
    wget -c --mirror -U "Mozilla" -p --convert-links http://docs.python-requests.org

httpie


"""

