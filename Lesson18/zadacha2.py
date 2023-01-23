# {'b':2,'d':4,'a':1}
# a=1 b=2 d=4

def query(params):
    return sorted(f'{k}={v}' for k,v in params.items())

print(query({'b':2,'d':4,'a':1}))