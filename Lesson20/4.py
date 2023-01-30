def func():
   data = []
   line = None
   linecount = 0
   while True:
       part = yield line
       linecount += part.count('\n')
       data+=part
       if linecount > 0:
           index = data.index('\n')
           line =''.join(data[:index+1])
           data = data[index+1:]
           linecount -= 1
       else:
           line = None
r = func()
print(r.send(None))
print(r.send('hello'))
print(r.send('world\nit '))
print(r.send('works!'))
print(r.send('\n'))
