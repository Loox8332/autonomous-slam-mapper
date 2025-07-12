#include <iostream>
#include <limits>

int main()
{
    int num1 {};
    int num2 {};
    int num3 {};

    std::cout << "Enter three number: ";
    std::cin >> num1 >> num2 >> num3;

    std::cout << "Number entered " << num1 << ", " << num2 << " and " << num3 << ".";
}
