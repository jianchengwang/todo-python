
import re

content = 'Xiaoshuaib has 100 bananas'
res = re.match('^Xi.*?(\\d+)\\s.*s$',content)
print(res.group(1))

content = """Xiaoshuaib has 100 
bananas"""
res = re.match('^Xi.*?(\\d+)\\s.*s$',content,re.S)
print(res.group(1))

res = re.search('Xi.*?(\\d+)\\s.*s',content,re.S)
print(res.group(1))

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\\d+)\\s.*?s;',content,re.S)
print(res)
