"""
curl 的使用 apt install curl
注意 安装的时候可能会遇到 openssl报错 有可能 openssl 未安装

    -A 设置 user-agent curl -A "Chrome" https://www.baidu.com
    -X 用指定方法请求 curl -X POST http://httpbin.org/post
    -I 只返回请求头信息
    -d 以 POST 方法 请求 url 并发送相应的参数
            curl -d "test=123&b=2&c=3&d=4" http://httpbin.org/post
            curl -d @file 《文件》
                 -d a=1 -d b=2 -d c=3
    -O 下载文件并以远程的文件名保存 curl -O http://httpbin.org/image/jpeg
    -o 下载文件并以指定文件名保存 curl -o fox.jpeg http://httpbin.org/image/jpeg
    -L 跟随重定向请求 curl -IL https://baidu.com
    -H 设置头信息 curl -o image.webp -H "accept:image/webp" http://httpbin.org/image
    -k 允许发起不安全的SSL 请求
    -b 设置cookies curl -b a=test http://httpbin.org/cookies
    -s 不显示其他无关信息
    alias myip="curl http://httpbin.org/get|grep -s -E 'origin' | cut -d '\"' -f4"   
"""

"""
wget



"""