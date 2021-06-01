def extract_full_name(names):
    return [''.join(x['first'] + ' ' + x['last']) for x in names]


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
