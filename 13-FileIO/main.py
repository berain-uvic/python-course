import re

pattern = re.compile('11/2/2021')

a = pattern.fullmatch('1/2/2021')
print(a)