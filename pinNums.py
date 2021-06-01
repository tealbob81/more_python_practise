lst = [9,8,5,6,2,3]

for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            for l in range(len(lst)):
                print(f'{lst[i]} : {lst[j]} : {lst[k]} : {lst[l]}')
                #print('('+str(lst[i]) + ','+ str(lst[j]) + ',' + str(lst[k])+ ',' + str(lst[l] + ')\n'))
