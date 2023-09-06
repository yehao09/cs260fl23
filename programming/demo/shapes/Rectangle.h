#include <iostream>

#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
    private: 
        int x;
        int y;

    public:
        // constructors
        Rectangle() {
            std::cout<<"\n Default constructor executed \n";
            x = y = 1;
        }

        Rectangle(int x, int y) {
            std::cout << "\n Overloaded constructors, with two parameters ";
            std::cout << x << " " << y << "\n";
            this->x = x;
            this->y = y;
        }

        // destructor
        ~Rectangle(){
            std::cout<<"\n Destructor executed \n";
        }

        // accessors: setters getters
        int getX(){
            return this->x;
        }

        int getY(){
            return this->y;
        }

        void setX(int x){
            this->x = x;
        }

        void setY(int y){
            this->y = y;
        }


        // calculates and returns the area of the Rectangle
        int area() {
            return x * y;
        }

        // calculates and returns the perimeter of the Rectangle
        int perimeter() {
            return 2 * (x + y);
        }

        // we also have friends
        friend std::ostream& operator<<(std::ostream &out, const Rectangle &r);
};


// not part of the class, overloaded * operator
// used to repeat a string
std::string operator * (const std::string src, unsigned int rep) {
  std::string out = "";
  while (rep--) {
    out += src;
  }
  return out;
}

// friend of the class, overloaded << operator
// allows us to use cout << RectangleObj
std::ostream& operator<< (std::ostream &out, const Rectangle &r) {
  std::string middleDash = "---";
  std::string plus = "+";
  std::string pipe = "┆";
  std::string middleSpace = "   ";
  unsigned int row = 1;

  out << "\n" << plus << middleDash * r.x << plus << "\n";
  while(row++ <= r.y) {		
    out << pipe << middleSpace * r.x << pipe << std::endl; 
  }
  out << plus << middleDash * r.x << plus << std::endl;

  return out;
}


#endif      //RECTANGLE_H

    
