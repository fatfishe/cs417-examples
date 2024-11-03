#include <iostream>
#include <iomanip>

#include <math>


void sqrt_demo()
{
    for (unsigned int power = 0; power < 20; ++power) {
        const double result = std::sqrt(1 + pow(10, -power));
        // print(f" sqrt(1 + 10^-{power:<2d}) = {result:>50.50f}")
    }
}

int main()
{
    sqrt_demo();

    return 0;
}
