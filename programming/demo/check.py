def f1(a,b):
    return a or b

def f2(a,b):
    return a or (not a and b)

def f3(a,b):
    return (not a and b ) or (a and not b) or (a and b)


'''
    a function of N variables will ahve a truth table with 2**N rows
        2 variable yields 2**2 = 4 rows

    Therefore, we will test our funcitons with the following boolean values:
               a  b
     test 1:   0  0
     test 2:   0  1
     test 3:   1  0
     test 4:   1  1

    see: https://realpython.com/python-assert-statement/
'''


# test 1: 0 0
a = False
b = False
assert f1(a,b) == f2(a,b) and f2(a,b) == f3(a,b), "error on 0 0"

# test 2: 0 1 
a = False
b = True
assert f1(a,b) == f2(a,b) and f2(a,b) == f3(a,b), "error on 0 1"

# test 3: 1 0 
a = True
b = False
assert f1(a,b) == f2(a,b) and f2(a,b) == f3(a,b), "error on 1 0"

# test 4: 1 1
a = True
b = True
assert f1(a,b) == f2(a,b) and f2(a,b) == f3(a,b), "error on 1 1"

print("done, looks good to me")

