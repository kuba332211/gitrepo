#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_cw2.py

def main(args):
    n = int(input("podaj 1. liczbę"))
    while n < 1: 
        print("Błędne dane!")
        n = int(input("podaj 1. liczbę"))
        
    m = int(input("podaj 2. liczbę"))
    while m <= n:
        print("Błędne dane!")
        m = int(input("podaj 2. liczbę"))
#pobieranie        

    for liczba in range (n, m + 1):
        print (liczba, " ", end="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
