from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import re

with open('20200830_180146RTLS_log.txt') as fin:
    text = fin.read();
    regex = r':\[([\s\S]*?)\]:'
    matches = re.findall(regex, text)
    strsx = []
    strsy = []
    strsz = []
    for match in matches:
        words = match.split(',')
        strsx.append(words[0])
        strsy.append(words[1])
        strsz.append(words[2])

x1 = list(map(float, strsx))
y1 = list(map(float, strsy))

figsize = 11, 9
figure, ax = plt.subplots(figsize=figsize)

# 在同一幅图片上画两条折线
A, = plt.plot(x1, y1, '-r', label='A', linewidth=5.0)


# 将文件保存至文件中并且画出图
plt.savefig('figure.eps')
plt.show()