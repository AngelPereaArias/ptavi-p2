#!/usr/bin/python3
# -*- coding: utf-8 -*

import sys


class Calculadora:
    op1 = 0
    op2 = 0
    
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2
    
    def plus(op1, op2):
        """ Function to sum the operands """
        return op1 + op2
        
    def minus(op1, op2):
        """ Function to substract the operands """
        return op1 - op2


if __name__ == "__main__":
    try:
        op1 = int(sys.argv[1])
        op2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
        
    if sys.argv[2] == "suma":
        result = Calculadora.plus(op1, op2)
    elif sys.argv[2] == "resta":
        result = Calculadora.minus(op1, op2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

    print(result)
