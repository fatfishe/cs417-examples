#! /usr/bin/env python3

import math
import sys

from parseTemps import (parse_raw_temps)


if __name__ == "__main__":

    input_temps = sys.argv[1]
    includes_units = sys.argv[2] == "yes"  # set to False for files without units

    print(includes_units)

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file, units=includes_units):
            print(temps_as_floats)
