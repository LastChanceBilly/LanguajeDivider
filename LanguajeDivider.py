#!/bin/python2
from __future__ import print_function
import sys

def main():
    archivo = None
    try:
        archivo = open("Languajes.txt", "r+")
    except:
        directory = raw_input("Locacion del archivo: ")
        try:
            archivo = open(directory, "r+")
        except:
            print("No se a encontrado el archivo")
    lines = 0
    for line in archivo:
        print(lines, end='')
        print("> ", end='')
        print(line, end='')
        lines += 1
if __name__ == '__main__':
    main()
