// overloading class constructors
#include "alphabet.h"
#include <cassert>

int main () {

  Alphabet abBase10;   // default constructor
  Alphabet abBase2 (2);   // base=2 as arg
  Alphabet abBase8 (8);   // base=8 as arg
  Alphabet abBase16 (16); // base=16


  std::cout << "Print alphabet of symbols using the overloaded operato <<\n";
  std::cout << "alphabetdefault base 10 (decimal): " << abBase10<< std::endl;
  std::cout << "alphabetbase 2 (binary): " << abBase2<< std::endl;
  std::cout << "alphabetbase 8 (octal): " << abBase8<< std::endl;
  std::cout << "alphabetbase 16 (hexadecimal): " << abBase16<< std::endl;
  std::cout << std::endl;

  std::cout << "test size() method, print the size of alphabet of symbols.\n";
  std::cout << "alphabetbase 10 size(): " << abBase10.size()<< std::endl;
  std::cout << "alphabetbase 2 size(): " << abBase2.size()<< std::endl;
  std::cout << "alphabetbase 8 size(): " << abBase8.size()<< std::endl;
  std::cout << "alphabetbase 16 size(): " << abBase16.size()<< std::endl;
  std::cout << std::endl;


  std::cout << "using assert to test subscript operator [].\n";
  assert(abBase10[0] == '0');
  std::cout << "first index abBase10 OK.\n";
  assert(abBase10[abBase10.size() - 1] == '9');
  std::cout << "last index abBase10 OK.\n";

  assert(abBase2[0] == '0');
  std::cout << "first index abBase2 OK.\n";
  assert(abBase2[abBase2.size() - 1] == '1');
  std::cout << "last index abBase2 OK.\n";

  assert(abBase8[0] == '0');
  std::cout << "first index abBase8 OK.\n";
  assert(abBase8[abBase8.size() - 1] == '7');
  std::cout << "last index abBase2 OK.\n";

  assert(abBase16[0] == '0');
  std::cout << "first index abBase16 OK.\n";
  assert(abBase16[abBase16.size() - 1] == 'f');
  std::cout << "last index abBase16 OK.\n";
  std::cout << std::endl;

  std::cout << "test maxValid() method, print last valid symbol from alphabet in red color.\n";
  std::cout << "alphabetbase 16 maxValid: " << abBase10.maxValid()<< std::endl;
  std::cout << "alphabetbase 2 maxValid: " << abBase2.maxValid()<< std::endl;
  std::cout << "alphabetbase 8 maxValid: " << abBase8.maxValid()<< std::endl;
  std::cout << "alphabetbase 16 maxValid: " << abBase16.maxValid()<< std::endl;
  std::cout << std::endl;

  return 0;
}