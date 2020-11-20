my_sty = 'a中国'
print(my_sty, type(my_sty))
# str --> bytes
my_sty_utf8 = my_sty.encode('utf-8')
print(my_sty_utf8)
my_sty_gbk = my_sty.encode('gbk')
print(my_sty_gbk)
# bytes --> str 编码需要保持一致
my_sty_gbk.decode('gbk')
my_sty_utf8.decode('utf-8')


