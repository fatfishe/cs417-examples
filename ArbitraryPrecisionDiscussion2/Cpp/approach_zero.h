#include <iostream>
#include <iomanip>
#include <cmath>

#ifndef APPROACH_ZERO_H_INCLUDED
#define APPROACH_ZERO_H_INCLUDED

using std::right;
using std::setw;
using std::cout;

/**
 * Evaluate a given function (f) for x values in the range 1 to 2^(-2000)
 * where each value is have the previous one (1, 0.5, 0.25, 0.125...)
 *
 * @tparam F any function or function-like (i.e., callable) type that takes a
 *           single double and returns a single double
 *
 * @param f mathematical function to evaluate
 */
template<typename F>
void approach_zero(F f)
{
    for (int i = 0; i < 2000; ++i) {
        const double x = pow(2, -i);
        const double f_of_x = f(x);

        std::cout.setf(std::ios::showpoint | std::ios::scientific);
        std::cout.precision(20);

        cout << "2^-" << i << " / "
             << right << setw(24) << x << " | "
             << right << setw(24) << f_of_x << '\n';
    }
}

#endif
