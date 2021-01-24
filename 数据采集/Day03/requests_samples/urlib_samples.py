import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')
# 读取 response 的内容
text = r.read().decode()

# http 返回的状态码和msg
print(r.status, r.reason)

# 返回的内容是json格式 直接用Load函数加载
obj = json.loads(text)
print(obj)

# r.headers 是一个HTTPMessage对象
print(r.headers)
for k, v in r.headers._headers:
    print(f'{k, v}')
print('#' * 100)
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/87.0.4280.88 Safari/537.36'

# 添加自定义头信息
req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-Agent', ua)
# 接受一个 urlib.request.Request对象作为参数
r = urllib.request.urlopen(req)
resp = json.load(r)
# 打印出 httpbin 网站返回信息里的user-agent
print('user-agent:', resp['user-agent'])
print('#' * 100)
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='httpbin auth',
#                           uri='/basic-auth/123/123',
#                           user='123',
#                           passwd='123')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# r = urllib.request.urlopen('http://httpbin.org')
# print(r.read().decode())
# 使用 GET 参数
print('#' * 100)
params = urllib.parse.urlencode({'a': 1})
url = f'http://httpbin.org/get?{params}'
with urllib.request.urlopen(url) as f:
    print(json.load(f))
print('#' * 100)
# 使用 POST 参数
data = urllib.parse.urlencode({'a': 1})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))
print('#' * 100)
# 使用代理IP 请求远程url
proxy_handler = urllib.request.ProxyHandler({
    'socks5': 'socks5://124.42.7.103:80'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler() # 需要用户名密码时

opener = urllib.request.build_opener(proxy_handler)
r = opener.open('http://httpbin.org/ip')
print(r.read())
print('#' * 100)

# urlparse 模块
o = urllib.parse.urlparse('http://httpbin.org/get?a=1#test')
print(f'{o.scheme},{o.netloc},{o.fragment},{o.query},{o.username},{o.geturl()}')
print(list(o))
