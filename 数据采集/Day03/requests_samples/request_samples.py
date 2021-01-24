import requests

# GET 请求
r = requests.get('http://httpbin.org/get')
print(r.status_code, r.reason)
print(r.text)

# 带参数的 GET 请求
r = requests.get('http://httpbin.org/get', params={'a': 1, 'b': 2})
r = requests.get('http://httpbin.org/get?a=1&b=2')
print('GET 请求', r.json())
print('')
# POST 请求
r = requests.post('http://httpbin.org/post', data={'a': '1'})
print('POST 请求', r.json())
print('')

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/87.0.4280.88 Safari/537.36'

headers = {
    'User-Agent': ua
}

r = requests.get('http://httpbin.org/headers', headers=headers)
print('自定义headers请求', r.json())

# 带 cookie 的请求

cookies = dict(userid='123456', token='xxxxxxxxxxxxxxxxxx')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print('带cookies的请求', r.json())

# BASIC-AUTH 认证请求
r = requests.get('http://httpbin.org/basic-auth/123/123', auth=('123', '123'))
print(r'带cookies的请求', r.text)

bad_r = requests.get('http://httpbin.org/status/404')
print('主动返回错误代码', bad_r.status_code)
try:
    bad_r.raise_for_status()
except Exception as e:
    print(e)

# 使用requests.Session对象请求
# 创建一个Session对象
s = requests.Session()
# session对象会保存目标服务器返回的set-cookies 头信息里面的内容
s.get('http://httpbin.org/cookies/set/userid/123456789')
s.get('http://httpbin.org/cookies/set/token/xxxxxxxxxxx')
# 下一次请求会将本地所有的cookies信息自动添加到请求头信息里面
r = s.get('http://httpbin.org/cookies')
print('session 中的cookies', r.json())

# 在 requests 中使用代理
print('不使用代理', requests.get('http://httpbin.org/ip').json())
print('使用代理', requests.get('http://httpbin.org/ip', proxies={'http': 'http://www.fannstar.cn:41801'}).json())
try:
    r = requests.get('http://httpbin.org/delay/4', timeout=5)
except requests.exceptions.ReadTimeout as e:
    print(e)
else:
    print('指定等待时间', r.text)
