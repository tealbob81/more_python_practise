

def calculate(make_float, operation, message, **kwargs):
    operation_lookup = dict(add = '+', subtract = '-', multiply = '*', divide = '/')
    if make_float == True:
        return f'{message} {kwargs["first"]} {operation_lookup[operation]} {kwargs["second"]}'
print(calculate(make_float=True, operation='add', message='You just added ', first=2, second=3))
        
        
