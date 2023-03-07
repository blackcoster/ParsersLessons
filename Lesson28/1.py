import re
# 1. хотя бы 1 буква a          a a*
# 2. ровно 5 букв b             bbbbb
# 3.произовольное четное число букв c (cc)*
# 4.в конце d или e             (d|e)



match = re.search(r'aa*bbbbb(cc*(d|e))', r'aaabbbbbcce')
print(match[0] if match else 'Not found')
r'https.*'