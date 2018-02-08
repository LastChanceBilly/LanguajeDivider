#!/bin/python2
import sys

def main():
    archivo = " "
    try:
        open("Languajes.txt", "r+")
    except:
        directory = raw_input("Locacion del archivo: ")
        try:
            archivo = open(directory, "r+")
        except:
            print("No se a encontrado el archivo")
if __name__ == '__main__':
    main()
