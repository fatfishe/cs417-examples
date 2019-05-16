#include <cmath>
#include <cfloat>
#include <iostream>
#include <iomanip>

#include <quadmath.h>

/*
namespace std {
    __float128 abs( __float128 x )
    {
        return x;
    }
}
*/

template<typename T>
T estimatePrecision()
{
    T a = (4.0 / 3.0);
    T b = a - 1.0;
    T c = b + b + b;

    return std::abs(c - 1.0);
}


int main(int argc, char** argv)
{
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " num_execs" << "\n";
        return 1;
    }

    long num_execs = std::stol(argv[1]);

    long start = time(NULL);

    float sp;
    double dp;
    //__float128 qp;

    for (long i = 0; i < num_execs ; i++) {
        sp = estimatePrecision<float>();
        dp = estimatePrecision<double>();
        //qp = estimatePrecision<__float128>();
    }

    long stop = time(NULL);

    std::cout << sp << "\n"
              << dp << "\n";
              //<< qp << "\n";

    //printf("%.36Qg\n", qp);

    std::cout << (stop - start) << " secs" << "| " << num_execs << " # executions" << "\n";

    return 0;
}
