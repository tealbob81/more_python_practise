def intersection(l1, l2):
    l1.extend(l2)
    for i in l1:
        if l1.count(i) == 1:
            l1.remove(i)
    set_list = set(l1)
    result = list(set_list)
    return result
    

print(intersection([1,2,3], [2,3,4]))

