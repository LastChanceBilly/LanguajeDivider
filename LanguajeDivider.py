#!/bin/python2
from __future__ import print_function
import sys
from random import shuffle

def main():
    #Default directory for the input file
    directory = "Languajes.txt"
    archivo = None
    #Try to open it, if you can't, ask for its location
    try:
        archivo = open(directory, "r+")
        print("Archivo '{0}' encontrado".format(directory))
    except:
        directory = raw_input("Locacion del archivo: ")
        try:
            archivo = open(directory, "r+")
        except:
            print("No se a encontrado el archivo")
    #Get the amount of lines from the file and print it
    lines = 0
    for line in archivo:
        print(lines, end='')
        print("> ", end='')
        print(line, end='')
        lines += 1
    #We are done with the file for now, close it
    archivo.close()
    #Get the amount of groups from the user
    grupos = raw_input("Cantidad de grupos: ")
    groups = 0
    try:
        groups = int(grupos)
    except:
        print("Valor Invalido")
    #Get the amount of projects per group and show it
    try:
        NumPgroup = int(lines/groups)
    except:
        print("Valor Invalido")
    print("Temas por grupo: ", end='')
    print(NumPgroup)
    #Create a new list with all the values in between 0 - [number of lines]
    listadoShuff = list(range(lines))
    #Shuffle it
    shuffle(listadoShuff)
    #Open the file again
    archivo = open(directory, "r+")
    #For each group...
    for a in range(groups):
        print (a + 1, end='')
        print (":")
        #Get from where on the list this group's projects begins, and end
        for x in range(NumPgroup * a, (NumPgroup * a) + NumPgroup):
            #Print them
            print(" ", end='')
            print(listadoShuff[x], end='')
            print(" ", end='')
            print(archivo.readline(x))
    #Close file
    archivo.close()
if __name__ == '__main__':
    main()
