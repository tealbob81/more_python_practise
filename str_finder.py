def string_finder(lst):
    ''' Returns true if all items in list are strings'''
    return all([type(x) == str for x in lst])

l = ['gg', 'ff', 'what']
print(string_finder(l))
