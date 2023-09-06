#include "Rectangle.h"

int main() {
    Rectangle r = Rectangle(2,3);
    std::cout << "\n area: " << r.area();
    std::cout << "\n perimeter: " << r.perimeter();
    std::cout << r;

    std::cout << "\n getX: " << r.getX();
    std::cout << "\n getY: " << r.getY();
    std::cout << "\n calling setX and setY with new values\n";     
    r.setX(5);
    r.setY(10);
    std::cout << "\n getX: " << r.getX();
    std::cout << "\n getY: " << r.getY();

    std::cout << "\n area: " << r.area();
    std::cout << "\n perimeter: " << r.perimeter();
    std::cout << r;

    return 0;
}
