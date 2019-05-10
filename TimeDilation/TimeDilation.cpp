#include <iostream>
#include <math.h>
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

// Constants
const double MPH_TO_M_DIV_S = 0.44704;
const double C              = 299791958; // speed of light (m/s)
const double C_SQUARED      = C * C;

const std::string DIVIDER(32, '-');

int main(int argc, char**  argv)
{
    double gamma     = 0.0;
    double gamma_inv = 0.0;

    double proper_time = 0.0;
    double time        = 1; //in hours

    double diff = 0.0;

    const int days_per_week  = 5;
    const int weeks_per_year = 16 * 2;
    const int drive_duration = 60; // length of drive one way in minutes

    time = 2 * days_per_week
         * weeks_per_year
         * drive_duration * 60 ; //time driving to/from odu in one year in seconds

    cout.setf(ios::fixed);
    setprecision(8);

    for(double speed = 10; speed <= 60; speed += 5)
    {
        double speed_in_ms = (speed * MPH_TO_M_DIV_S);

        gamma     = 1.0 / sqrt(1 - pow((speed_in_ms / C), 2));
        gamma_inv = (C_SQUARED - (.5 * pow(speed_in_ms, 2.0))) / C_SQUARED;

        proper_time = time / gamma_inv;

        diff = time - proper_time;

        cout << "Mph          " << right << setw(19) << speed       << "\n";
        cout << "m/s          " << right << setw(19) << speed_in_ms << "\n";
        
        cout << DIVIDER << "\n";
        cout << "Gamma        " << right << setw(19) << gamma       << "\n";
        cout << "Gamma inv    " << right << setw(19) << gamma_inv   << "\n";
        
        cout << DIVIDER << "\n";
        cout << "Time         " << right << setw(19) << time        << "\n";
        cout << "Time(proper) " << right << setw(19) << proper_time << "\n";
        cout << "Difference   " << right << setw(19) << diff        << "\n"
             << "\n";
    }

    return 0;
}
