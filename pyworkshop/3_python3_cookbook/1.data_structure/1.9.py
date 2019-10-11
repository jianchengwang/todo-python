# 查找两字典的相同点

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# Find keys in common
print(a.keys() & b.keys())
# Find keys in a that are not in b
print(a.keys() - b.keys())
# Find (key, value) pairs in common
print(a.items() & b.items())

# Tips 
# keys()返回键视图，items()返回元素视图，都支持集合操作，比如交，并，差运算
# values() 不支持上述的集合操作