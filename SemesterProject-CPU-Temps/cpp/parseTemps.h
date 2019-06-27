#ifndef PARSE_TEMPS_H_INCLUDED
#define PARSE_TEMPS_H_INCLUDED

#include <iostream>
#include <iomanip>
#include <vector>
#include <iterator>
#include <algorithm>
#include <utility>

/**
 * A pair of values where the
 *   - _first_ attribute represents the time at which the readind was taken
 *   - _second is a vector with _n_ temperature readings, where _n_ is the
 *     number of CPU Cores
 */
using CoreTempReading = std::pair<int, std::vector<double>>;

/**
 * Take an input file and time-step size and parse all core temps.
 *
 * @param original_temps an input file
 * @param step_size time-step in seconds
 *
 * @return a vector of 2-tuples (pairs) containing time step and core
 *         temperature readings
 */
std::vector<CoreTempReading> parse_raw_temps(std::istream& original_temps,
                                             int step_size = 30);

#endif
