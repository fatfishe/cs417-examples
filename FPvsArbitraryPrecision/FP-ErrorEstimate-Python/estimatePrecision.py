#! /usr/bin/env python3

import math
import sys
import time
import typing

from decimal import (Decimal)
import decimal
from fractions import Fraction


def estimate_precision_float():
    a = (4.0 / 3.0)
    b = a - 1.0
    c = b + b + b

    return math.fabs(c - 1.0)


def estimate_precision_float_type_hints() -> float:
    a = (4.0 / 3.0)  # type: float
    b = a - 1.0      # type: float
    c = b + b + b    # type: float

    return math.fabs(c - 1.0)


def estimate_precision_decimal() -> Decimal:
    a = Decimal(4.0) / Decimal(3.0)
    b = a - Decimal(1.0)
    c = b + b + b

    return abs(c)


def perform_execs(est_func, num_execs):
    """
    Run an arbitrary function a predefined number of times.

    :param est_func: estimation function to run
    :param num_execs: number of function executions

    :return: 2-tuple containing estimated precions and total execution time
    """

    start = time.time()

    for i in range(0, num_execs):
        x = est_func()

    stop = time.time()
    total_time = stop - start

    return (x, total_time)


def main():
    if len(sys.argv) < 2:
        print("Usage: {} num_execs".format(sys.argv[0]))
        sys.exit(1)

    num_execs = 0
    try:
        num_execs = int(sys.argv[1])

    except ValueError as e:
        sys.exit(1)

    if len(sys.argv) == 3:
        decimal.getcontext().prec = int(sys.argv[2])

    precision = decimal.getcontext().prec

    estimate_functions = [("float", estimate_precision_float),
                          ("float-type-hint", estimate_precision_float_type_hints),
                          ("Decimal-{}".format(precision), estimate_precision_decimal)]

    for label, function in estimate_functions:
        estimate, total_time = perform_execs(function, num_execs)

        print("{:>16}|{:>5.4f}|{}".format(label, total_time, estimate))


if __name__ == "__main__":
    main()
