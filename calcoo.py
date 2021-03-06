#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys


class Calculadora():

    def plus(self, op1, op2):
        """ Function to sum the operands """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2


if __name__ == "__main__":
    try:
        op1 = float(sys.argv[1])
        op2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = Calculadora().plus(op1, op2)
    elif sys.argv[2] == "resta":
        result = Calculadora().minus(op1, op2)
    else:
        sys.exit('Solo sumar, restar, multiplicar o dividir.')

    print(result)
