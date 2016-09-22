#!/usr/bin/python3
# -*- coding: utf-8 -*


import calcoohija
import sys
import csv

if __name__ == "__main__":

    lines = csv.reader(open('fichero', newline=''), delimiter=',')
    for line in lines:
        elems = ' '.join(line).split(" ")
        result = int(elems[1])

        if elems[0] == "suma":
            for elem in range(len(elems)-2):
                #print(str(result) + " + " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().plus(int(elems[elem+2]), result)
            
            
        elif elems[0] == "resta":
            for elem in range(len(elems)-2):
                #print(str(result) + " - " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().minus(result, int(elems[elem+2]))
            

        elif elems[0] == "multiplica":
            for elem in range(len(elems)-2):
                #print(str(result) + " * " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().multiply(int(elems[elem+2]), result)
            
        elif elems[0] == "divide":
            for elem in range(len(elems)-2):
                #print(str(result) + " / " + str(elems[elem+2]))
                result = calcoohija.CalculadoraHija().divide(result, int(elems[elem+2]))
            
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')

        print(str(result))
            
