def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return  f'{one}{delimiter}{two}'

print(get_summ('Learn', 'python'))
