#! /usr/bin/eny python

import math

if __name__ == "__main__":

    for d in range(0, 20):
        print("{:>50.20f}".format(math.sqrt(1 + 10 ** -d)))
