#! /usr/bin/env python3

import math
from decimal import *

# https://docs.python.org/3/library/decimal.html

def main():

    getcontext().prec = 32

    mphToMs   = Decimal("0.44704")
    c         = Decimal("299792458")
    c_sqrd    = c ** 2
    
    gamma     = 0.0
    gamma_inv = 0.0

    temp     = 0.0
    proptime = 0.0
    time     = 1.0 #in hours

    diff     = 0.0

    time = Decimal((2 * 5) * (16 * 2) * 3600) #time driving to/from odu in one year

    for speed in range(10, 65, 5):
        speed_in_ms = speed * mphToMs

        gamma     = 1.0 / math.sqrt( 1 - (speed_in_ms / c ** Decimal(2.0)) ) 
        gamma_inv = Decimal( c_sqrd - Decimal(Decimal(0.5) * speed_in_ms * speed_in_ms) ) / c_sqrd
        proptime  = time / gamma_inv

        diff = time - proptime
        
        print("-" * 40)
        print("MPH          ", speed)
        print("m/s          ", speed_in_ms)
        print("Gamma        ", gamma)
        print("Gamma inv    ", gamma_inv)
        print("Time         ", time)
        print("Time(proper) ", proptime)
        print("Difference   ", diff)

if __name__ == "__main__":
    main()
