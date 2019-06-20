#! /usr/bin/env python3

import math
import sys

from typing import (Callable, TextIO, Iterator, List, Tuple)


def parse_raw_temps(original_temps: TextIO,
                    step_size: int=30, units: bool=True) -> Iterator[Tuple[float, List[float]]]:
    """
    Take an input file and time-step size and parse all core temps.

    :param original_temps: an input file
    :param step_size:      time-step in seconds
    :param units: True if the input file includes units and False if the file
                  includes only raw readings (no units)

    :yields: A tuple containing the next time step and a List containing _n_
             core temps as floating point values (where _n_ is the number of
             CPU cores)
    """

    if units:
        for step, line in enumerate(original_temps):
            yield (step * step_size), [float(entry[:-2]) for entry in line.split()]
    else:
        for step, line in enumerate(original_temps):
            yield (step * step_size), [float(entry) for entry in line.split()]


if __name__ == "__main__":

    input_temps = sys.argv[1]

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            print(temps_as_floats)
