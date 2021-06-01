def triple_and_filter(nums):
    '''triples multiples of 4 in a list'''
    print([num*3 for num in nums if num % 4 == 0])

test = [1,2,4,8,12,23]
triple_and_filter(test)
