import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))

q = collections.deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
q.popleft()
print(q)

dd = collections.defaultdict(lambda: 'N/A')  # 使用dict 如果引用的key不存在就会抛出KeyError 如果希望key不存在时 返回一个默认值 就可以使用defaultdict
dd['key1'] = 'abc'
print(dd['key2'])  # 除了key不存在时的返回值 其他行为都是一样的

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

c = collections.Counter()  # 简单的计数器
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)