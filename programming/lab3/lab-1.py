'''
Task-0 expanded:
    Use the code from lab-1 to create a function definition.
    * function header is provided to indicate:
       function name
       function input parameters
       function output data type
       docstring indicates what the function should return 

    * replace pass keyword in the function body with code from lab-1.

'''

def get_int(num: str, base = 10) -> int:
    ''' returns decimal integer representation of num '''
    pass


"""

sample code from lab-1 if you need it.

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

# num = input("please enter a number number: ")
# base = int(input("please enter a base: "))

index = 0
exponent = len(num) - 1

result_value = 0 # accumulator

while exponent >=0:
    result_value += lookup_table[num[index]] * base**exponent
    index += index
    exponent -= 1


# a) print original value and its data type
print( num, type(num))
# b) print resulting value and its data type
print(result_value, type(result_value))
"""
