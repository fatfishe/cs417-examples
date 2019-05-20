#! /usr/bin/env python3

import math
import sys
import time
import typing

from decimal import (Decimal)
import decimal
from fractions import Fraction

import cleve_moler as cm


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
        print(f"Usage: {sys.argv[0]:} num_execs [arbitrary precision]")
        sys.exit(1)

    num_execs = 0
    try:
        num_execs = int(sys.argv[1])

    except ValueError as e:
        sys.exit(1)

    if len(sys.argv) == 3:
        decimal.getcontext().prec = int(sys.argv[2])

    precision = decimal.getcontext().prec

    estimate_functions = [("float", cm.estimate_precision_float),
                          ("float-type-hint", cm.estimate_precision_float_type_hints),
                          (f"Decimal-{precision:}", cm.estimate_precision_decimal)]

    for label, function in estimate_functions:
        estimate, total_time = perform_execs(function, num_execs)

        print(f"{label:>16}|{total_time:>7.4f}|{estimate:}")


if __name__ == "__main__":
    main()
