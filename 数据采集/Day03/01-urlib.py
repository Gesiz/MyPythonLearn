import urllib
from pprint import pprint

# pprint(dir(urllib))
import json
from urllib.request import urlopen

r = urlopen('http://httpbin.org/get')
text = r.read().decode("utf-8")
print(json.loads(text))  # 查看返回的信息

print(f'r.status  返回的状态为 : {r.status}')
print(f'r.reason  返回的结果为 : {r.reason}')

print(f'r.headers 返回对象结果 : {r.headers}')
print(f'r.headers.get_all(Content-Type) : {r.headers.get_all("Content-Type")}')
print(f'r.headers.keys() : {r.headers.keys()}')
print(f'r.headers.values() : {r.headers.values()}')
print(f'_headers : {dict(r.headers._headers)}')

