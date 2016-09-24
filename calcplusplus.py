#!/usr/bin/python3
# -*- coding: utf-8 -*

import calcplus
import calcoohija
import sys
import csv


if __name__ == "__main__":

    lines = csv.reader(open('fichero', newline=''), delimiter=',')
    for line in lines:
        elems = ' '.join(line).split(" ")

        print(calcplus.operation(elems))
