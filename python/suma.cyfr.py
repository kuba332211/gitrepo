#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma.cyfr.py

def sumuj_cyfry1(liczba):
    suma = 0
    
    while liczba> 0:
        suma = suma + (liczba % 10)
        liczba = int(liczba / 10)

def main(args):
    n = int(input("podaj liczbę dwucyfrową"))
    while n < 10: 
        print("Błędne dane!")
        n = int(input("podaj liczbę dwucyfrową"))
        
        
    suma = 0
    
    while n > 0:
        suma = suma + (n % 10)
        liczba = int(n / 10)
        
    print("Suma:", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
