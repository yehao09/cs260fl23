#include <iostream>
#include <string>
#include <unordered_map>
#include <cmath>
#include <iomanip>


#ifndef ALPHABET_H
#define ALPHABET_H

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"
#define ANSI_BOLD          "\x1b[1m"


// define lookup table 'key:char' -> 'value:int'
static const std::unordered_map<char, int> lookup_table1 = {
    { '0', 0 },
    { '1', 1 },
    { '2', 2 },
    { '3', 3 },
    { '4', 4 },
    { '5', 5 },
    { '6', 6 },
    { '7', 7 },
    { '8', 8 },
    { '9', 9 },
    { 'a', 10 },
    { 'b', 11 },
    { 'c', 12 },
    { 'd', 13 },
    { 'e', 14 },
    { 'f', 15 }
};

// define lookup table 'key:int' -> 'value:char'
static const std::unordered_map<int, char> lookup_table2 = {
    { 0, '0' },
    { 1, '1' },
    { 2, '2' },
    { 3, '3' },
    { 4, '4' },
    { 5, '5' },
    { 6, '6' },
    { 7, '7' },
    { 8, '8' },
    { 9, '9' },
    { 10, 'a' },
    { 11, 'b' },
    { 12, 'c' },
    { 13, 'd' },
    { 14, 'e' },
    { 15, 'f' }
};

// define lookup table 'key:char' -> 'value:std::string'
static const std::unordered_map<char, std::string> lookup_table3 = {
    { '0', "0" },
    { '1', "1" },
    { '2', "2" },
    { '3', "3" },
    { '4', "4" },
    { '5', "5" },
    { '6', "6" },
    { '7', "7" },
    { '8', "8" },
    { '9', "9" },
    { 'a', "a" },
    { 'b', "b" },
    { 'c', "c" },
    { 'd', "d" },
    { 'e', "e" },
    { 'f', "f" }
};

// define lookup table for base 
static const std::unordered_map<int, std::string> lookup_base = {
    { 2, "binary" },
    { 8, "octal" },
    { 10, "decimal" },
    { 16, "hexadecimal" }
};


// class definition 
class Alphabet {
  private: 
    int base;       // indicate the base for the alphabet
    int SIZE;       // same as base
    char *symbols;  // alphabet of symbols as pointer

  public:
    Alphabet ();     // constructor default, uses base 10
    Alphabet (int);  // costructor, specify base as argument
    int size();      // returns SIZE of alphabet
    std::string maxValid(); // returns last valid symbol as string, in red color

    // operator overloading, for printing 
    friend std::ostream& operator<< (std::ostream &output, const Alphabet& A );

    // operator overloading, subscript []
    char& operator[](const int index );
    ~Alphabet() { delete [] symbols ; } // destructor
}; 


Alphabet::Alphabet () {
    base = 10;
    SIZE = 10;
    symbols = new char[SIZE];
    for(int i=0; i < SIZE; i++){
        symbols[i] = lookup_table2.at(i);
    }
}

Alphabet::Alphabet (int base) {
    base = base;
    SIZE = base;
    symbols = new char[SIZE];
    for(int i=0; i < SIZE; i++){
      symbols[i] = lookup_table2.at(i);
    }
}

int Alphabet::size(){
    return this->SIZE;
}

std::string Alphabet::maxValid(){
    return ANSI_COLOR_RED +  lookup_table3.at( symbols[ SIZE - 1 ] ) + ANSI_COLOR_RESET;
}

std::ostream& operator<< (std::ostream &output, const Alphabet& A ) { 
    output << "{ ";
    for(int i=0; i<A.SIZE; i++){
        output << "'" << A.symbols[i];
        if (i != A.SIZE-1)
            output <<  "', ";
        else
            output <<  "' }";
    }
    return output;            
}

char& Alphabet::operator[](const int index ) { 
    if( index > SIZE ) {
       std::cout << "index out of range" << std::endl;
       // Or raise error
       return this->symbols[0];
     }
     return this->symbols[index];
}


#endif 
