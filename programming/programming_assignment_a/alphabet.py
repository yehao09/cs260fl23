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
        2:"binary",
        8:"octal",
        10:"decimal",
        16:"hexadecimal"
}


# class definition 
class Alphabet:
    def __init__(self, base = 10):
        """ constructor """
        # Note: 'private' variables do not exist in Python classes
        #   see https://docs.python.org/3/tutorial/classes.html#tut-private
        #   Python does not prevent us from access to: obj._base, obj._Alphabet__base   
        self._base = base     # indicate the base for the alphabet
        self.__base = base    # or __var, to avoid name clashes by using name mangling
        self._size = base     # same as base
        self._symbols =  list(hexdigits[:base]) # alphabet of symbols 
            
    def size(self):
        """ return size of alphabet """
        return self._size

    def max_valid(self):
       """ returns highest value of alphabet - color coded in red """
       # Note: you can also use a module, e.g. https://pypi.org/project/colorama/
       return ANSI_COLOR_RED    + self._symbols[-1] + ANSI_COLOR_RESET   

    def __repr__(self):
        """ provide string representation  """
        # note: you can define __str__ instead of __repr__
        # however if __str__ is not defined it falls back on __repr__
        # also see: https://realpython.com/python-repr-vs-str/
        return '{' + str( self._symbols )[1:-1] + '}'

    def __getitem__(self, index):
        """ subscript operator: obj[i] returns alphabet element at i """
        # see: https://docs.python.org/3/reference/datamodel.html#object.__getitem__
        return self._symbols[index] 



if __name__ == "__main__":
    """ the below code executes when alphabet.py runs as a script,
        but will NOT execute when File is imported as a module 
    see: https://realpython.com/if-name-main-python/ """
    print(lookup_base[10])
    a1  = Alphabet() # default argument value for base is 10
    print('string representation:', a1)  # test string representation of object
    print('max_valid():',a1.max_valid())  
    print('size()',a1.size())
    print('subscript [0]', a1[1]) # expected '0' 
    print('subscript [-1]', a1[-1]) # expected '9' 
    print()

    base = 2
    print(lookup_base[base])
    a2 = Alphabet(base)
    print('string representation:', a2)  # test string representation of object
    print('max_valid():',a2.max_valid())  
    print('size()', a2.size())
    print('subscript [0]', a2[1]) # expected '0' 
    print('subscript [-1]', a2[-1]) # expected '1' 
    print()

    base = 8
    print(lookup_base[base])
    a8 = Alphabet(base)
    print('string representation:', a8)  # test string representation of object
    print('max_valid():',a8.max_valid())  
    print('size()',a8.size())
    print('subscript [0]', a8[1]) # expected '0' 
    print('subscript [-1]', a8[-1]) # expected '7' 
    print()

    base = 16
    print(lookup_base[base])
    a16  = Alphabet(base)
    print('string representation:', a16)  # test string representation of object
    print('max_valid():',a16.max_valid())  
    print('size()',a16.size())
    print('subscript [0]', a16[1]) # expected '0' 
    print('subscript [-1]', a16[-1]) # expected 'f' 
    print()
    
    # no private variables
    print(f'Python classes do not not have {ANSI_COLOR_RED} "private" {ANSI_COLOR_RESET} members:')
    print('You should still define/use getters as proper programming practice!')
    print('Direct access to variables with dot operator is bad practice:')
    print('  Python does not prevent us from access to: obj._base, obj._Alphabet__base')   
    print('  a16._base:', a16._base)
    print('  a16._Alphabet__base:', a16._Alphabet__base)
    print('  see https://docs.python.org/3/tutorial/classes.html#tut-private')


