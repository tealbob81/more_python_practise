def alphabet_position(text):
    nums = [i for i in range(1,27)]
    chars = [chr(i) for i in range(97,123)]
    my_dict = dict(zip(chars,nums))
    result = []
    for i in text.lower():
         result.append(str(my_dict.get(i, '')))
    end = ' '.join(result)
    return ' '.join(end.split())
    

print(alphabet_position("The narwhal bacons at midnight."))
