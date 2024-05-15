#! /usr/bin/env python3

import decimal
import math
import sys
import time
import typing
from decimal import Decimal
from fractions import Fraction

import cleve_moler as cm


def perform_execs(est_func, num_execs):
    """
    Run an arbitrary function a predefined number of times.

    Args:
        est_func: estimation function to run
        num_execs: number of function executions

    Returns:
        2-tuple containing estimated precions and total execution time
    """

    start = time.time()

    #  for i in range(0, num_execs):
    for _ in range(0, num_execs):
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

    except ValueError as _e:
        sys.exit(1)

    if len(sys.argv) == 3:
        decimal.getcontext().prec = int(sys.argv[2])

    precision = decimal.getcontext().prec

    estimate_functions = [
        ("float", cm.estimate_precision_float),
        ("float-type-hint", cm.estimate_precision_float_type_hints),
        (f"Decimal-{precision:}", cm.estimate_precision_decimal),
    ]

    for label, function in estimate_functions:
        estimate, total_time = perform_execs(function, num_execs)

        print(f"{label:>16}|{total_time:>7.4f}|{estimate:}")


if __name__ == "__main__":
    main()
