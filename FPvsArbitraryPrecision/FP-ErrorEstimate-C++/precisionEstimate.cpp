#include <cmath>
#include <cfloat>
#include <iostream>
#include <iomanip>

// Use Boost float128
#include <boost/multiprecision/float128.hpp>

using namespace boost::multiprecision;

// An ugly bodge
namespace std {
    float128 abs(float128 x)
    {
        return x;
    }
}

template<typename T>
T estimatePrecision()
{
    T a = (4.0 / 3.0);
    T b = a - 1.0;
    T c = b + b + b;

    return std::abs(c - 1.0);
}

template<>
float128 estimatePrecision<float128>()
{
    using T = float128;

    T a = (4.0Q / 3.0Q);
    T b = a - 1.0Q;
    T c = b + b + b;

    return (c - 1.0Q);
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
    float128 qp; // float128 is added by boost

    for (long i = 0; i < num_execs ; i++) {
        sp = estimatePrecision<float>();
        dp = estimatePrecision<double>();
        qp = estimatePrecision<float128>();
    }

    long stop = time(NULL);

    std::cout << sp << "\n"
              << dp << "\n"
              << qp << "\n";

    std::cout << (stop - start) << " secs" << "| " << num_execs << " # executions" << "\n";

    return 0;
}
