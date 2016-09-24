#!/usr/bin/python3
# -*- coding: utf-8 -*

import calcoohija
import sys


def operation(elems):

    result = float(elems[1])
    operation_range = range(len(elems)-2)
    for elem in operation_range:
        operand = float(elems[elem+2])
        if elems[0] == "suma":
            result = calcoohija.CalculadoraHija().plus(result, operand)
        elif elems[0] == "resta":
            result = calcoohija.CalculadoraHija().minus(result, operand)
        elif elems[0] == "multiplica":
            result = calcoohija.CalculadoraHija().multiply(result, operand)
        elif elems[0] == "divide":
            result = calcoohija.CalculadoraHija().divide(result, operand)
        else:
            sys.exit('Solo sumar, restar, multiplicar o dividir.')
    return result


if __name__ == "__main__":

    try:
        document = open(sys.argv[1])
    except ValueError:
        sys.exit("Error: Invalid Document")

    lines = document.readlines()

    for line in lines:
        elems = line.split(",")
        print(operation(elems))
