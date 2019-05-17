#include <cmath>
#include <iostream>
#include <iomanip>
#include <functional>

#include "cleveMoler.h"


/**
 * Run an arbitrary function a predefined number of times.
 *
 * @param f function to run
 * @param num_execs number of function executions
 *
 * @return total execution time
 */
template<typename T>
long performExecs(T (*f)(), long num_execs)
{
    long start = time(NULL);
    T p;

    for (long i = 0; i < num_execs ; i++) {
        p = f();
    }

    long stop = time(NULL);

    return stop - start;
}

//------------------------------------------------------------------------------
int main(int argc, char** argv)
{
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " num_execs" << "\n";
        return 1;
    }

    long num_execs = std::stol(argv[1]);

    float sp;
    double dp;
    float128 qp; // float128 is added by boost

    /*
    std::cout << sp << "\n"
              << dp << "\n"
              << qp << "\n";
    */

    std::cout << performExecs(estimatePrecision<float>, num_execs) << " secs"
              << " | "
              << num_execs << " # executions" << "\n";
    std::cout << performExecs(estimatePrecision<double>, num_execs) << " secs"
              << " | "
              << num_execs << " # executions" << "\n";
    std::cout << performExecs(estimatePrecision<float128>, num_execs) << " secs"
              << " | "
              << num_execs << " # executions" << "\n";

    return 0;
}
