import math
from string import hexdigits

ANSI_COLOR_RED     =  "\x1b[31m"
ANSI_COLOR_GREEN   =  "\x1b[32m"
ANSI_COLOR_YELLOW  =  "\x1b[33m"
ANSI_COLOR_BLUE    =  "\x1b[34m"
ANSI_COLOR_MAGENTA = "\x1b[35m"
ANSI_COLOR_CYAN    = "\x1b[36m"
ANSI_COLOR_RESET   = "\x1b[0m"
ANSI_BOLD          = "\x1b[1m"

lookup_table1 = {
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

lookup_table2 = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f'
}


# define lookup table for base 
lookup_base = {
    2, "binary",
    8, "octal",
    10, "decimal",
    16, "hexadecimal"
}


# class definition 
class Alphabet:
    def __init__(self, base = 10):
        """ constructor """
        self.base = base     # indicate the base for the alphabet
        self.SIZE = base     # same as base
        self.symbols =  list(hexdigits[:base]) # alphabet of symbols 
        # Note: 'private' variables do not exist in Python classes
        #   see https://docs.python.org/3/tutorial/classes.html#tut-private

    def size(self):
        """ return size of alphabet """
        return self.SIZE

    def maxValid(self):
       """ returns highest value of alphabet - color coded in red """
       # Note: you can also use a module, e.g. https://pypi.org/project/colorama/
       return ANSI_COLOR_RED    + self.symbols[-1] + ANSI_COLOR_RESET   

    def __repr__(self):
        """ provide string representation  """
        # note: you can define __str__ instead of __repr__
        # however if __str__ is not defined it falls back on __repr__
        # also see: https://realpython.com/python-repr-vs-str/
        return '{' + str( self.symbols )[1:-1] + '}'

    def __getitem__(self, index):
        """ subscript operator: obj[i] returns alphabet element at i """
        # see: https://docs.python.org/3/reference/datamodel.html#object.__getitem__
        return self.symbols[index] 



if __name__ == "__main__":
    """ the below code executes when alphabet.py runs as a script,
        but will NOT execute when File is imported as a module 
    see: https://realpython.com/if-name-main-python/ """
    print(a1)
    print(a1.maxValid()) 
    print(a1.size())
    print(a1[1]) # expected '1' 
    print(a1[9]) # expected '9' 


    a1  = Alphabet(base = 16)
    print(a1)
    print(a1.maxValid()) 
    print(a1.size())
    print(a1[1]) # expected '1' 
    prin
    t(a1[15]) # expected 'f' 



