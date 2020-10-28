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

first_2000 = list(map(float, strsx))
second_2000 = list(map(float, strsy))
third_2000 = list(map(float, strsz))


# print to check data
print(f"{first_2000}")
print(f"{second_2000}")
print(f"{third_2000}")

# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure1 = ax.plot(first_2000, second_2000, third_2000, c='r')
plt.show()