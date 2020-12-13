ilist = [1, [1,2,3], 3, [1,2,[4,5,6]], 5, 6, 7, 8, 9]

def plist(m):
    for i in m:
        if type(i) == list:
            plist(i)
        else:
            print(i)

plist(ilist)
