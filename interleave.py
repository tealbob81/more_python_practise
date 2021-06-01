def interleave(str1, str2):
    ''' returns two strings interwoven'''
    
    #mixed_tuple = list(zip(str1, str2))
    #unpacked_lst = [''.join(c) for c in mixed_tuple]

    return ''.join(''.join(x) for x in (zip(str1,str2)))

print(interleave('hi', 'ho'))
