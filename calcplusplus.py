#!/usr/bin/python3
# -*- coding: utf-8 -*

import calcoohija
import sys
import csv

if __name__ == "__main__":

    lines = csv.reader(open('fichero', newline=''), delimiter=',')
    for line in lines:
        elems = ' '.join(line).split(" ")
        result = float(elems[1])

        if elems[0] == "suma":
            for elem in range(len(elems)-2):
                # prfloat(str(result) + " + " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().plus(float(elems[elem+2]), result)

        elif elems[0] == "resta":
            for elem in range(len(elems)-2):
                # prfloat(str(result) + " - " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().minus(result, float(elems[elem+2]))

        elif elems[0] == "multiplica":
            for elem in range(len(elems)-2):
                # prfloat(str(result) + " * " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().multiply(float(elems[elem+2]), result)

        elif elems[0] == "divide":
            for elem in range(len(elems)-2):
                # prfloat(str(result) + " / " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().divide(result, float(elems[elem+2]))

        else:
            sys.exit('Solo sumar, restar, multiplicar o dividir.')

        print(str(result))            
