#! /usr/bin/env python3

import math
import sys
import time
import typing

from decimal import (Decimal)
import decimal


def estimatePrecisionFloat():
    a = (4.0 / 3.0)
    b = a - 1.0
    c = b + b + b

    return math.fabs(c - 1.0)


def estimatePrecisionFloatTypeHints() -> float:
    a = (4.0 / 3.0)  # type: float
    b = a - 1.0      # type: float
    c = b + b + b    # type: float

    return math.fabs(c - 1.0)


def estimatePrecisionDecimal() -> Decimal:
    a = Decimal(4.0) / Decimal(3.0)
    b = a - Decimal(1.0)
    c = b + b + b

    return abs(c)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: {} num_execs [float|arbitrary] [arbitrary precision]")
        sys.exit(1)

    num_execs = 0
    try:
        num_execs = int(sys.argv[1])
    except ValueError as e:
        sys.exit(1)

    estimation_function = estimatePrecisionFloat
    est_type = "float"

    if len(sys.argv) == 3:
        est_type = sys.argv[2]

    if est_type == "arbitrary":
        estimation_function = estimatePrecisionDecimal

    elif est_type == "float-th":
        estimation_function = estimatePrecisionFloatTypeHints

    if len(sys.argv) == 4:
        decimal.getcontext().prec = int(sys.argv[3])

    start = time.time()

    for i in range(0, num_execs):
        x = estimation_function()

    stop = time.time()
    total_time = stop-start

    print(f"{total_time:0.8f} secs | {num_execs:>10} executions")
