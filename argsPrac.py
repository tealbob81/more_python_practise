##def ensure_correct_info(*args):
##    if 'Bear' in args and 'Goodman' in args:
##        return 'Welcome back Bear'
##    return 'Not sure who you are'
##
##print(ensure_correct_info())
##print(ensure_correct_info(1, True, 'Bear', False, 'Goodman'))


##def fav_colours(**kwargs):
##    for person,colour in kwargs.items():
##        print(f'{person.title()}\'s favourite colour is {colour}.')
##
##fav_colours(bear='purple', cat='white', lynsay='grey')
##
    
##def special_greeting(**kwargs):
##    if 'Bear' in kwargs and kwargs['Bear'] == 'special':
##        return 'You get a special greeting Bear!'
##    elif 'Bear' in kwargs:
##        return f'{kwargs["Bear"]} Bear!'
##
##    return 'Not sure who this is...'
##
##print(special_greeting(Bear='Hello'))
##print(special_greeting(David='Hello'))
##print(special_greeting(Bear='special'))
##

##def combine_words(word,**kwargs):
##    
##    if 'prefix' in kwargs:
##        return f'{kwargs["prefix"]}{word}'
##    elif 'suffix' in kwargs:
##        return f'{word}{kwargs["suffix"]}'
##
##    return word
##print(combine_words('child'))
##print(combine_words('child', prefix='man'))
##print(combine_words('child', suffix='ish'))

##
##def sum_all_values(*args):
##    total = 0
##    for num in args:
##        total += num
##    print(total)
##nums = [1,2,3,4,5,6]
##sum_all_values(*nums)
##def add_and_multiply_numbers(a,b,c,**kwargs):
##    print(kwargs)
##    print(a + b * c)
##data = {'a': 1, 'b': 2, 'c': 3}
##add_and_multiply_numbers(**data, d=7)

def calculate(make_float, operation, message, **kwargs):
    operation_lookup = dict(add = '+', subtract = '-', multiply = '*', divide = '/')
    if make_float == True:
        return f'{message} {kwargs["first"] operation_lookup[operation] kwargs["second"]}'
print(calculate(make_float=True, operation='add', message='You just added ', first=2, second=3))
        
        
