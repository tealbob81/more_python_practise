def order(sequence):
    result = []
    slst = []
    seq_lst = sequence.split(' ')
    for i in sequence:
        if i.isdigit():
            result.append(i)
    new = dict(zip(sorted(result),seq_lst))
    #for num in sorted(result):
        #if num in sequence:
            #slst.insert(int(num)-1,seq_lst[int(num)-1])
    return new
            



     



##    for i in sequence:
##        if i.isdigit():
##            print(sequence.index(i))
##
##


print(order("is2 Thi1s T4est 3a"))
