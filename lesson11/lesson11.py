import os
# os.system('kover.jpg')
# os.system('11.txt')
# os.system('mkdir test')
# os.system('python test.py')

# with open ("lang.txt") as file:
#     str1 = file.read()
# print(str1)

# with open ("lang.txt") as file:
#     str1 = file.readlines()
# print(str1)

with open ("lang.txt") as file:
    str1 = file.read()
wordlist=str1.split()
print(wordlist)

result ='';
for word in wordlist:
    result+=word+', '
print(result)

result2 = ','.join(wordlist)
print(result2)
