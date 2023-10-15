def weighted_sum(num: str, base = 2):
    ''' returns decimal integer representation of num '''

    '''
        s = "19.21"
        s[0]*10**1 + s[1]*10**0 + s[3]*10**-1 + s[4]*10**-2
         1            9            2            1


    '''

    print('input value: ', num)
    lookup_table = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15
    }

    index = 0
    exponent = len(num) - 1

    result_value = 0 # accumulator

    # iterate over the string containing the digits
    while exponent >= 0:
        result_value += lookup_table[num[index]] * base**exponent
        index += 1
        exponent -= 1

    return result_value
    

print('output value', weighted_sum('1011', base = 2) )  # input 1011 in base 2 --> expected output 11 as decimal
print('output value', weighted_sum('21', base = 8) )    # input 21 in base 8 --> expected output 17 in decimal
print('output value', weighted_sum('fe', base = 16) )    # input fe in base 16 --> expected output 256 in decimal