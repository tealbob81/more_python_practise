##def colorize(text, color):
##
##    colors = ('cyan', 'yellow', 'blue', 'red', 'green')
##
##    if type(text) != str:
##        raise TypeError('text muxt be a string')
##    if color not in colors:
##        raise ValueError('color is invalid')
##
##    print(f'Printed {text} in {color}')
##
##colorize('hello', 'red')
##colorize('hello', 'orange') #raises ValueError
##colorize(3, 'blue') #raises TypeError


##def get(d,key):
##    try:
##        return d[key]
##    except KeyError:
##        return None
##d = {"name": 'Bear'}
###d['city']
##
##print(get(d,'city'))

##while True:
##
##    try:
##        num = int(input('enter a num '))
##    except ValueError:
##        print('That is not a number')
##    else:
##        print('Good job')
##        break
##    finally:
##        print('will always run')
##
##print('game logic')
          
def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('do not divide by zero ..')
    except TypeError as err:
        print('You can not divide a letter silly')
        print(err)
    else:
        print(f'{a} divided by {b} is {result}')

print(divide(1,2))
print(divide(1,'a'))
#print(divide(1/0))

