# 解压序列赋值给多个变量

# 1.1.1
p = (4, 5)
a, b = p
print(a)
print(b)
# x, y, z = p Traceback (most recent call last):


# 1.1.2
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, month, day) = data
print(name)
print(year)

# 1.1.3
s = 'Hello'
a, b, c, _, _ = s
print(a)
print(c)