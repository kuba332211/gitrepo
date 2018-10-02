#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py

def main(args):
    n = int(input("podaj 1. liczbę"))
    while n < 1: 
        print("Błędne dane!")
        n = int(input("podaj 1. liczbę"))
        
#pobieranie        

    for liczba in range (n + 1):
        print (liczba * liczba, " ", end="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
