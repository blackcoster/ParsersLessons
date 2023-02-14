user_permissions=['admin']

def check_permission(permission):
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError('no prav')
                print('no prav')
            return func()

        return wrapped_check
    return wrapper_permission

@check_permission('user')
def check():
    return 'проверено'

@check_permission('admin')
def do():
    return 'правки внесены'
print(do())
print(check())

