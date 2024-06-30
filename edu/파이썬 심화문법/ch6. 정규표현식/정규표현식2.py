import re

# 1. group 그룹

str1 = '010-2343-333'
result = re.match('\d{2,3}-\d{3,4}-\d{4}$',str1)
print(result)