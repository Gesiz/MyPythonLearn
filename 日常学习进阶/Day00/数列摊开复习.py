iList = [1, [1, 2], 3, [3, 4, [5, 6]]]
iList = [[1, 2], [3, 4], [5, [6,7]]]
print([j for a in iList for j in a])
