#! /usr/bin/env python3

import sys

from decimal import (Decimal, getcontext)
# https://docs.python.org/3/library/decimal.html

C = Decimal("299792458")
C_SQRD = C ** 2
MPH_TO_MS = Decimal("0.44704")


def compute_gamma(speed):
    """
    Compute Gamma and Inverse Gamma

    Args:
        speed: travel speed in m/s
    """

    gamma     = Decimal(1.0) / Decimal.sqrt(1 - (speed / C) ** Decimal(2))
    gamma_inv = Decimal(C_SQRD - Decimal(Decimal(0.5) * speed * speed)) / C_SQRD

    # print(repr(1 - (speed / C_SQRD)))

    return (gamma, gamma_inv)


def main():

    if len(sys.argv) > 1:
        getcontext().prec = int(sys.argv[1])
    else:
        getcontext().prec = 32

    driving_time = Decimal((2 * 5) * (16 * 2) * 3600)  # time driving to/from odu in one year

    for speed in range(10, 65, 5):
        speed_in_ms = speed * MPH_TO_MS

        gamma, gamma_inv = compute_gamma(speed_in_ms)

        proptime = driving_time / gamma_inv

        diff = driving_time - proptime

        print("-" * (14 + getcontext().prec + 2))
        print(f"MPH           {speed}")
        print(f"m/s           {speed_in_ms}")
        print(f"Gamma         {gamma}")
        print(f"Gamma inv     {gamma_inv}")
        print(f"Time          {driving_time}")
        print(f"Time (proper) {proptime}")
        print(f"Time (proper) {driving_time * gamma}")
        print(f"Difference    {diff}")


if __name__ == "__main__":
    main()
