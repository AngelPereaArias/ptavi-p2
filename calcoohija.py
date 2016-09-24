#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):
    def multiply(self, op1, op2):
        """ Function to multiply the operands """
        return op1 * op2

    def divide(self, op1, op2):
        """ Function to divide the operands """
        try:
            return op1 / op2
        except:
            sys.exit("Error: Unable to divide by zero")

if __name__ == "__main__":
    try:
        op1 = float(sys.argv[1])
        op2 = float(sys.argv[3])

    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = CalculadoraHija().plus(op1, op2)

    elif sys.argv[2] == "resta":
        result = CalculadoraHija().minus(op1, op2)

    elif sys.argv[2] == "multiplica":
        result = CalculadoraHija().multiply(op1, op2)

    elif sys.argv[2] == "divide":
        result = CalculadoraHija().divide(op1, op2)

    else:
        sys.exit('Solo sumar, restar, multiplicar o dividir')

    print(result)
