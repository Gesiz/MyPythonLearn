import re
with open('20200830_180146RTLS_log.txt') as fin, open('2.txt', 'w') as fout:
    text = fin.read();
    regex = r':\[([\s\S]*?)\]:'
    matches = re.findall(regex, text)
    strsx = []
    strsy = []
    strsz = []
    for match in matches:
        fout.write(match)
        words = match.split(',')
        strsx.append(words[0])
        strsy.append(words[1])
        strsz.append(words[2])

strsx = list(map(float, strsx))
strsy = list(map(float, strsy))
strsz = list(map(float, strsz))

print(strsx)
print(strsy)
print(strsz)