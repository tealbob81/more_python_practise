import sys

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print('To do the same thing it take...')
print(f'List comp: {list_comp} bytes')
print(f'Generator Expression: {gen_exp} bytes')
