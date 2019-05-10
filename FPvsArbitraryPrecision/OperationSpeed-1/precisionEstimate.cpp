#include <cmath>
#include <iostream>
#include <iomanip>

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

    for (long i = 0; i < num_execs ; i++) {
        float  sp = estimatePrecision<float>();
        double dp = estimatePrecision<double>();
    }

    long stop = time(NULL);

    std::cout << (stop - start) << " secs" << "| " << num_execs << " # executions" << "\n";

    return 0;
}
