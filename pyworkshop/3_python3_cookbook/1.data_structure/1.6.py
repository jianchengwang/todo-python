# 字典中的键映射多个值

# 1.6.1
d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
print(d['a'])

# 1.6.2
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)