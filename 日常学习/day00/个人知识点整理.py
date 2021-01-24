# iList = [1, 2, 3]
# iList.insert(3, [1])
# iList.append([2])
# iList.extend([1])
# print(iList)
# iList.pop(3)
# iList.remove(3)
# print(iList)
# iSet = set()
# iSet.add()
# iSet.update()
#
# iSet.remove()
# iSet.discard()
# iSet.pop()
# iSet.clear()
#
# iDict = {}

from datetime import datetime
strtime1 = '2021-01-18'
strtime2 = '2022-01-19'
c1day = datetime.strptime(strtime1, '%Y-%m-%d')
c2day = datetime.strptime(strtime2, '%Y-%m-%d')

result = c2day-c1day
print(result.days)